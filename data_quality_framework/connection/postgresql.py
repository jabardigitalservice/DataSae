import os
from os.path import join, dirname
import csv
import json
from io import StringIO

from dotenv import load_dotenv
from psycopg2 import connect
from psycopg2.extras import execute_values
from sqlalchemy import create_engine
import pandas as pd


class Connection:
    def __init__(self, source, db_name):
        __file__ = 'connection/'
        dotenv_path = join(dirname(__file__), 'connection.env')
        # dotenv_path = 'connection.env'
        load_dotenv(dotenv_path)

        self.username = os.environ.get("POSTGRESQL_{}_USERNAME".format(source))
        self.password = os.environ.get("POSTGRESQL_{}_PASSWORD".format(source))
        self.host = os.environ.get("POSTGRESQL_{}_HOST".format(source))
        self.port = os.environ.get("POSTGRESQL_{}_PORT".format(source))
        self.database = db_name
        self.engine = None
        self.conn_engine = None
        self.conn = None
        self.cursor = None

    def connection(self, conn_type):
        if conn_type == 'engine':
            self.engine = create_engine('postgresql://{}:{}@{}:{}/{}'
                                        .format(self.username, self.password, self.host, self.port, self.database))
            self.conn_engine = self.engine.connect()
            print("Connect Engine Postgresql")
            return self.engine, self.conn_engine

        elif conn_type == 'cursor':
            self.conn = connect(
                user=self.username,
                password=self.password,
                host=self.host,
                port=self.port,
                database=self.database
            )
            self.cursor = self.conn.cursor()
            print("Connect Cursor Postgresql")
            return self.conn, self.cursor
        else:
            print("No Connection")
            raise ConnectionError

    def close(self):
        if self.engine:
            self.conn_engine.close()
            self.engine.dispose()
        if self.conn:
            self.cursor.close()
            self.conn.close()


class Get:
    def __init__(self, source, database):
        self.connection = Connection(source, database)
        self.engine = None
        self.conn = None
        self.allowed_return_value = ['dataframe', 'json']

        try:
            self.engine, self.conn = self.connection.connection('engine')
        except:
            raise ConnectionError('Connection error')

    def by_query(self, query, return_value):
        if return_value not in self.allowed_return_value:
            raise ValueError('return_type value is invalid')

        data = pd.read_sql_query(con=self.conn, sql=query)
        if return_value == 'dataframe':
            pass
        else:
            data = data.to_records(index=False)
        return data

    def by_table(self, schema, table, return_value):
        if return_value not in self.allowed_return_value:
            raise ValueError('return_type value is invalid')

        data = pd.read_sql_table(con=self.conn, schema=schema, table_name=table)
        if return_value == 'dataframe':
            pass
        else:
            data = data.to_records(index=False)
        return data

    def close(self):
        self.connection.close()


class Post:
    def __init__(self, source, database):
        self.connection = Connection(source, database)
        self.conn = None
        self.cursor = None
        self.engine = None
        self.conn_engine = None

    def insert_only(self, data, data_size, schema, table):
        if data_size == 'large':
            if isinstance(data, pd.DataFrame):
                pass
            elif isinstance(data, list):
                data = pd.DataFrame(data)
            else:
                print('data type error')
                raise ValueError

            if not self.engine:
                try:
                    self.engine, self.conn_engine = self.connection.connection('engine')
                except:
                    raise ConnectionError('Connection invalid')
            data.to_sql(schema=schema, name=table, index=False, con=self.conn_engine, method=psql_insert_copy,
                        if_exists='replace')

        elif data_size == 'small':
            if isinstance(data, list):
                pass
            elif isinstance(data, pd.DataFrame):
                data = data.to_json(orient="records")
                data = json.loads(data)
            else:
                print('data type error')
                raise ValueError

            if not self.conn:
                try:
                    self.conn, self.cursor = self.connection.connection('cursor')
                except:
                    raise ConnectionError('Connection invalid')

            column = list(data[0].keys())
            insert_query = """
                INSERT INTO {}.{} ({})
                VALUES %s
                ON CONFLICT
                DO NOTHING""".format(schema, table, ','.join(column))
            insert_execute(self.conn, self.cursor, insert_query, data)
        else:
            raise ValueError

    def upsert(self, data, schema, table, list_key, list_update):
        if not self.conn:
            try:
                self.conn, self.cursor = self.connection.connection('cursor')
            except:
                raise ConnectionError('Connection invalid')

        column = list(data[0].keys())
        query_update = ''

        for i, update in enumerate(list_update, 1):
            if i == len(list_update):
                update = '{} = EXCLUDED.{}'.format(update, update)
            else:
                update = '{} = EXCLUDED.{}, '.format(update, update)
            query_update = query_update + update

        insert_query = """
            INSERT INTO {}.{} ({})
            VALUES %s
            ON CONFLICT ({})
            DO UPDATE SET {}""".format(schema, table, ','.join(column), ','.join(list_key), query_update)
        insert_execute(self.conn, self.cursor, insert_query, data)

    def update(self, data, insert_type, schema, table,):
        pass

    def delete_data(self, schema, table):
        query_delete = "DELETE FROM {}.{}".format(schema, table)
        self.conn.execute(query_delete)

    def close(self):
        self.connection.close()


def connect_metadata_airflow_k8s () :
    dotenv_path = join(dirname(__file__), 'connection.env')
    load_dotenv(dotenv_path)
    # COREDATA
    username = os.environ.get('POSTGRESQL_COREDATA_USERNAME')
    password = os.environ.get('POSTGRESQL_COREDATA_PASSWORD')
    host = os.environ.get('POSTGRESQL_COREDATA_HOST')
    port = os.environ.get('POSTGRESQL_COREDATA_PORT')
    database = 'metadata'

    engine_c = create_engine(
        'postgresql://{}:{}@{}:{}/{}'.format(username, password, host, port, database))

    return engine_c

def psql_insert_copy(table, conn, keys, data_iter):
    # gets a DBAPI connection that can provide a cursor
    dbapi_conn = conn.connection
    with dbapi_conn.cursor() as cur:
        s_buf = StringIO()
        writer = csv.writer(s_buf)
        writer.writerows(data_iter)
        s_buf.seek(0)

        columns = ', '.join('"{}"'.format(k) for k in keys)
        if table.schema:
            table_name = '{}.{}'.format(table.schema, table.name)
        else:
            table_name = table.name

        sql = 'COPY {} ({}) FROM STDIN WITH CSV'.format(
            table_name, columns)
        cur.copy_expert(sql=sql, file=s_buf)


def insert_execute(conn, cursor, query, data):
    column = list(data[0].keys())
    final_list_data = []

    for data in data:
        dat = []
        for col in column:
            dat.append(data[col])
        final_list_data.append(tuple(dat))

    execute_values(
        cursor, query, final_list_data, template=None, page_size=100
    )
    conn.commit()

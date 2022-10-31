import os
from dotenv import load_dotenv
from datasae.datasource.config_file import get_config
from cassandra.cluster import Cluster


class ConnectionCassandra:
    """
        A class to represent Cassandra access and datasource.

        ...

        Attributes
        ----------
        env_file_location : str
            your .env file path
        yaml_file_location : str
            your .yaml file path

        .. note::
            format for .yaml file
                datasource:
                    postgresql:
                        username : test
                        password : test
                        host : 109.102.102.11
                        port : 5432
                        db_name : postgres
                    cassandra:
                        username : test
                        password : test
                        host : 109.102.102.11
                        port : 5432
                        keyspace : test

            format for .env file
                username=test
                password=test
                host=10.10.0.17
                port=5432
                db_name=test

        Methods
        -------
        get_session():
            return engine data type for connected to mysql
    """
    def __init__(self, env_file_location=None, yaml_file_location=None):
        if env_file_location is not None:
            load_dotenv(env_file_location)
            host = os.environ.get('host')
            port = os.environ.get('port')
            keyspace = os.environ.get('keyspace')
        elif yaml_file_location is not None:
            config_yaml = get_config(yaml_file_location)
            host = config_yaml['datasource']['mysql']['host']
            port = config_yaml['datasource']['mysql']['port']
            keyspace = config_yaml['datasource']['mysql']['keyspace']

        # https://towardsdatascience.com/getting-started-with-apache-cassandra-and-python-81e00ccf17c9
        cluster = Cluster([host], port=port)
        self.session = cluster.connect(keyspace, wait_for_all_pools=True)
        # session.execute('USE %s'.format(keyspace))
        # rows = session.execute('SELECT * FROM users')
        # for row in rows:
        # print(row.age,row.name,row.username)

    def get_session(self):
        """
            return engine data type for connected to cassandra

            Parameters
            ----------

            Returns
            -------
            engine
        """
        return self.session

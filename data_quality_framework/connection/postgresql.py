import os
from os.path import join, dirname

import pandas
from dotenv import load_dotenv
from sqlalchemy import create_engine

class Connection:
    def __init__(self,db_name):
        dotenv_path = join(dirname(__file__), 'credential/.env')
        load_dotenv(dotenv_path)

        # SATUDATA
        username = os.environ.get('DB_SATUDATA_USERNAME')
        password = os.environ.get('DB_SATUDATA_PASSWORD')
        host = os.environ.get('DB_SATUDATA_ADDRESS')
        port = os.environ.get('DB_PORT')

        self.engine = create_engine(
            'postgresql://{}:{}@{}:{}/{}'.format(username, password, host, port, db_name))

    def get_engine(self):
        return self.engine

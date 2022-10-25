import os
from dotenv import load_dotenv
from pymongo import MongoClient
from datasae.datasource.config_file import get_config


class ConnectionMongodb:
    """
        A class to represent mongodb access and datasource.

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
                    mongodb:
                        username : test
                        password : test
                        host : 109.102.102.11
                        port : 5432
                        db_name : mysql

            format for .env file
                username=test
                password=test
                host=10.10.0.17
                port=5432
                db_name=test

        Reference
        ---------
        https://www.mongodb.com/languages/python

        Methods
        -------
        get_engine():
            return engine data type for connected to postgresql
    """
    def __init__(self, env_file_location=None, yaml_file_location=None):
        if env_file_location is not None:
            load_dotenv(env_file_location)
            username = os.environ.get('username')
            password = os.environ.get('password')
            host = os.environ.get('host')
            db_name = os.environ.get('db_name')
        elif yaml_file_location is not None:
            config_yaml = get_config(yaml_file_location)
            username = config_yaml['datasource']['postgresql']['username']
            password = config_yaml['datasource']['postgresql']['password']
            host = config_yaml['datasource']['postgresql']['host']
            db_name = config_yaml['datasource']['postgresql']['db_name']

        # Provide the mongodb
        CS = "mongodb+srv://{}:{}@{}/".format(username, password, host)

        # Create a connection
        client = MongoClient(CS)

        self.engine = client[db_name]

    def get_engine(self):
        """
            return engine data type for connected to postgresql

            Parameters
            ----------

            Returns
            -------
            engine
        """
        return self.engine

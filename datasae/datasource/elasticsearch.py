import os
from dotenv import load_dotenv
from datetime import datetime
from datasae.datasource.config_file import get_config
from elasticsearch import Elasticsearch


class ConnectionElastic:
    """
        A class to represent Elastic access and datasource.
        source:
        - https://elasticsearch-py.readthedocs.io/en/v7.17.7/
        - https://elasticsearch-py.readthedocs.io/en/v7.17.7/async.html

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
                    elasticsearch:
                        username : test
                        password : test
                        host : 109.102.102.11
                        port : 5432
                        index : test

            format for .env file
                username=test
                password=test
                host=10.10.0.17
                port=5432
                index=test

        Methods
        -------
        get_engine():
            return engine data type for connected to mysql
    """
    def __init__(self, env_file_location=None, yaml_file_location=None):
        if env_file_location is not None:
            load_dotenv(env_file_location)
            username = os.environ.get('username')
            password = os.environ.get('password')
            host = os.environ.get('host')
            port = os.environ.get('port')
            self.index = os.environ.get('index')
        elif yaml_file_location is not None:
            config_yaml = get_config(yaml_file_location)
            username = config_yaml['datasource']['elasticsearch']['username']
            password = config_yaml['datasource']['elasticsearch']['password']
            host = config_yaml['datasource']['elasticsearch']['host']
            port = config_yaml['datasource']['elasticsearch']['port']
            self.index = config_yaml['datasource']['elasticsearch']['index']

        self.es = Elasticsearch(
            ['https://{}:{}@{}:{}'.format(username, password, host, port)]
        )

    def get_engine(self):
        """
            return engine data type for connected to elastic.
            you can use pluggy to change into asycn or something new

            Parameters
            ----------

            Returns
            -------
            engine
        """
        return self.es

    def async_access(self):
        # https://elasticsearch-py.readthedocs.io/en/v7.17.7/async.html
        pass

    def sample_access(self):
        doc = {
            'author': 'kimchy',
            'text': 'Elasticsearch: cool. bonsai cool.',
            'timestamp': datetime.now(),
        }
        res = self.es.index(index="test-index", id=1, document=doc)
        print(res['result'])

        res = self.es.get(index="test-index", id=1)
        print(res['_source'])

        self.es.indices.refresh(index="test-index")

        res = self.es.search(index="test-index", query={"match_all": {}})
        print("Got %d Hits:" % res['hits']['total']['value'])
        for hit in res['hits']['hits']:
            print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])

import os
from os.path import join, dirname

from dotenv import load_dotenv
import requests


class Connection:
    def __init__(self, source):
        __file__ = 'connection/'
        dotenv_path = join(dirname(__file__), 'connection.env')
        # dotenv_path = 'connection.env'
        load_dotenv(dotenv_path)

        self.auth_type = os.environ.get("API_{}_AUTH_TYPE".format(source))
        self.test_endpoint = os.environ.get("API_{}_TEST_ENDPOINT".format(source))
        self.url = os.environ.get("API_{}_URL".format(source))

        if self.auth_type == 'basic':
            self.username = os.environ.get("API_{}_USERNAME".format(source))
            self.password = os.environ.get("API_{}_PASSWORD".format(source))

    def test_connection(self):
        pass


class Get:
    pass


class Post:
    def __init__(self, source):
        self.connection = Connection(source)

    def process(self, headers=None, data=None, timeout=None):
        if self.connection.auth_type == 'basic':
            data = requests.post(self.connection.url, auth=(self.connection.username, self.connection.password),
                                 headers=headers, data=data, timeout=timeout)
        return data.json()


class Auth:
    def basic(self):
        pass

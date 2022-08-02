import io
import json
from os.path import join, dirname

import pluggy
from datasae.datasource.google import GoogleSheet
from datasae.datasource.minios3 import MinioS3

hookspec = pluggy.HookspecMarker("data-quality-framework-datasae")
hookimpl = pluggy.HookimplMarker("data-quality-framework-datasae")


class MySpec:
    """A hook specification namespace."""

    @hookspec
    def myhook(self, url_link: str, sheet_name: str, creds: dict):
        """My special little hook that you can customize."""
        print('hook specs ....')
        # connect to minio
        obj = MinioS3('D:/repository/data-quality-framework/tests/credential/.env')
        credential_location = obj.return_minio_object('public')

        data = credential_location.get_object(
            bucket_name='dwhhistoryupload',
            object_name='users/jds_googlesheet_dataengineergmail.json'
        )

        print(data)
        creds = json.load(io.BytesIO(data.data))
        print(type(creds))
        obj = GoogleSheet('https://docs.google.com/spreadsheets/d/1rrhloohPqGKo5LRE2RmkuBFzFyrx-FttiWy_GQ7p8uk/',
                          'STAT - AKUMULASI HARIAN', creds)
        obj.transform_to_dataframe()


class Plugin_1:
    """A hook implementation namespace."""

    @hookimpl
    def myhook(self, url_link: str, sheet_name: str, creds: str):
        print("inside Plugin_1.myhook()")
        print(creds)
        return url_link


class Plugin_2:
    """A 2nd hook implementation namespace."""

    @hookimpl
    def myhook(self, url_link: str, sheet_name: str, creds: dict):
        print("inside Plugin_2.myhook()")
        return sheet_name


# create a manager and add the spec
pm = pluggy.PluginManager("data-quality-framework-datasae")
pm.add_hookspecs(MySpec)

# register plugins
pm.register(Plugin_1())
pm.register(Plugin_2())

results = pm.hook.myhook(url_link = 'https://docs.google.com/spreadsheets/d/1rrhloohPqGKo5LRE2RmkuBFzFyrx-FttiWy_GQ7p8uk/',
                          sheet_name = 'STAT - AKUMULASI HARIAN', creds = None)
print(results)

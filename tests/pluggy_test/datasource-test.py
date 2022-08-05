"""
this is docstring
"""
import io
import json

import pluggy
from datasae.datasource.google import GoogleSheet
from datasae.datasource.minios3 import MinioS3

hookspec = pluggy.HookspecMarker("data-quality-framework-datasae-datasource")
hookimpl = pluggy.HookimplMarker("data-quality-framework-datasae-datasource")


class GoogleSheetSpec:
    """A hook specification namespace."""

    @hookspec
    def transform_to_dataframe(self, url_link: str, sheet_name: str, creds: dict):
        """My special little hook that you can customize."""
        print('hook specs ....')
        obj = GoogleSheet(url_link, sheet_name, creds)
        obj.transform_to_dataframe()


class Plugin1:
    """A hook implementation namespace."""

    @hookimpl
    def transform_to_dataframe(self, url_link: str, sheet_name: str):
        """

        :param url_link:
        :param sheet_name:
        :return:
        """
        print("inside Plugin_1.myhook()")
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

        obj = GoogleSheet(url_link, sheet_name, creds)
        obj.transform_to_dataframe()

        return url_link


# create a manager and add the spec
pm = pluggy.PluginManager("data-quality-framework-datasae-datasource")
pm.add_hookspecs(GoogleSheetSpec)

# register plugins
pm.register(Plugin1())

results = pm.hook.transform_to_dataframe(
    url_link='https://docs.google.com/spreadsheets/d/1EW89UZnnUOQibt0KEjZXMmPu33YPu20TWntBpMkeplA/',
    sheet_name='Sheet1')
print(results)

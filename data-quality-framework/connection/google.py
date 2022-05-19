from os.path import join, dirname

import pandas as pd
import gspread
from dotenv import load_dotenv
from oauth2client.service_account import ServiceAccountCredentials
from minio import Minio
from sqlalchemy import create_engine
from datetime import datetime, timedelta
import os, pandas
import io
import json, requests

class GoogleSheet:
    def __init__(self, url_link: str, sheet_name: str):
        self.url_link = url_link
        self.sheet_name = sheet_name
        self.data_frame = None

        # connect to minio
        dotenv_path = join(dirname(__file__), '.env')
        load_dotenv(dotenv_path)
        scope = ['https://spreadsheets.google.com/feeds',
                 'https://www.googleapis.com/auth/drive']

        self.credential_location = Minio(
            os.environ['minio_cluster'],
            access_key=os.environ['minio_access_key'],
            secret_key=os.environ['minio_secret_key'],
            secure=True,
        )
        self.scope = ['https://spreadsheets.google.com/feeds',
                 'https://www.googleapis.com/auth/drive']


    def transform_to_dataframe(self):
        data = self.credential_location.get_object(bucket_name='dwhhistoryupload',
                                                   object_name='users/jds_googlesheet_dataengineergmail.json')
        creds = json.load(io.BytesIO(data.data))
        credentials = ServiceAccountCredentials.from_json_keyfile_dict(creds, self.scope)
        gc = gspread.authorize(credentials)

        spreadsheets = None
        headers = None

        try:
            gsheet = gc.open_by_url(self.url_link)

            spreadsheets = gsheet.worksheet(self.sheet_name).get_all_values()
            # cleansing header, cek dulu baris pertama, jika tak ada berarti error
            dirty_headers = spreadsheets.pop(0)
            headers = self.get_header(dirty_headers)

            print("total rows before change to dataframe : {}".format(len(spreadsheets)))
            data = pd.DataFrame(spreadsheets, columns=headers)
            print("total rows after change to dataframe : {}".format(data.index))
            print(data.head(5))

            return data
        except Exception as e:
            print(e)

        return None



    def get_header(self, headers):
        for i in range(0, len(headers)):
            headers[i] = headers[i].lower().replace(" ", "_").replace("/", "_").replace("\\", "_").replace(
                ",", "_") \
                .replace(".", "_").replace("%", "persen").replace('\n', '_').replace('(', '').replace(')', '')

        return headers
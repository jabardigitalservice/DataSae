from typing import List
import logging

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


CLIENT_SECRET_FILE: str = 'creds.json'
TIMEZONE: str = 'Asia/Jakarta'
SHEETS: List[dict] = [
    {
        'sheet_name': 'Kantor Kecamatan Cianjur',
        'sheet_range': 'A:G',
    }]


def get_google_service(
    client_secret_file: str = CLIENT_SECRET_FILE,
    service_name: str = 'sheets',
    version: str = 'v4',
    scopes: list = [
        'https://www.googleapis.com/auth/spreadsheets'
    ],
    **kwargs
):
    # Google Sheet API > Python Quickstart
    # https://developers.google.com/sheets/api/quickstart/python#configure_the_sample
    # Download Folders and Files using Google Drive API and Python
    # https://hansheng0512.medium.com/download-folders-and-files-using-google-drive-api-and-python-1ad086e769b
    # https://github.com/hansheng0512/google-drive-and-python/blob/master/download.py

    creds = None
    service = None

    credentials = service_account.Credentials.from_service_account_file(
        client_secret_file
    )
    creds = credentials.with_scopes(scopes)

    try:
        service = build(service_name, version, credentials=creds, **kwargs)
    except HttpError as error:
        logging.error(error)

    return service, creds

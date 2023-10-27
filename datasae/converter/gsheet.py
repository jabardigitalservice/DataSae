#!/usr/bin/env python3

# Copyright (c) Free Software Foundation, Inc. All rights reserved.
# Licensed under the AGPL-3.0-only License. See LICENSE in the project root
# for license information.

"""Google Spreadsheet library."""

from __future__ import annotations
from dataclasses import dataclass
import logging
import warnings

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import gspread
from pandas import DataFrame

from . import DataSource


@dataclass(repr=False)
class GSheet(DataSource):
    """
    Represents a data source that connects to an Google Spreadsheet.

    Args:
        client_secret_file (str): path location credential google spreadsheet.
    """

    client_secret_file: str

    @property
    def connection(self) -> tuple:
        """
        Returns a connection to the Google Spreadsheet.

        Returns:
            tuple: service & creds from googleservice account.
        """
        creds = None
        service = None

        credentials = service_account.Credentials.from_service_account_file(
            super().connection['client_secret_file']
        )
        creds = credentials.with_scopes([
            'https://www.googleapis.com/auth/spreadsheets'
        ])

        try:
            service = build('sheets', 'v4', credentials=creds)
        except HttpError as error:
            logging.error(error)
            raise

        return service, creds

    def __call__(
        self, gsheet_id: str, sheet_name: str,
    ) -> DataFrame:
        """
        __call__ method.

        Converts the data from google spreadsheet into a
        Pandas DataFrame.

        Args:
            gsheet_id (str): The id from url spreadsheet.
            sheet_name (str): The name a sheet will get data.

        Returns:
            DataFrame: A Pandas DataFrame.
        """
        _, creds = self.connection

        with warnings.catch_warnings(record=True):
            warnings.simplefilter('always')
            data = gspread.authorize(creds).open_by_key(
                gsheet_id
            ).worksheet(sheet_name)

        # default index 0 jadi kolom
        data1 = data.get_all_records()
        data2 = DataFrame(data1)

        logging.debug(data2)
        return data2

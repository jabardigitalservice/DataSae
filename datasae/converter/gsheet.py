#!/usr/bin/env python3

# Copyright (C) Free Software Foundation, Inc. All rights reserved.
# Licensed under the AGPL-3.0-only License. See LICENSE in the project root
# for license information.

"""Google Spreadsheet library."""

from __future__ import annotations
from dataclasses import dataclass
import warnings

from google.oauth2.service_account import Credentials
import gspread
from pandas import DataFrame

from . import DataSource


@dataclass(repr=False)
class GSheet(DataSource):
    """
    Represents a data source that connects to an Google Spreadsheet.

    Args:
        client_secret_file (str): path location credential google spreadsheet.
        gsheet_id (str, optional): The ID of the Google Spreadsheet.
    """

    client_secret_file: str
    gsheet_id: str = None

    @property
    def connection(self) -> Credentials:
        """
        Returns a credential for the Google Spreadsheet.

        Returns:
            Credentials: Creds from googleservice account.
        """
        return Credentials.from_service_account_file(
            self.client_secret_file,
            scopes=['https://www.googleapis.com/auth/spreadsheets']
        )

    def __call__(
        self, sheet_name: str, gsheet_id: str = None
    ) -> DataFrame:
        """
        __call__ method.

        Converts the data from google spreadsheet into a
        Pandas DataFrame.

        Args:
            sheet_name (str): The name a sheet will get data.
            gsheet_id (str, optional): The ID of the Google Spreadsheet.

        Returns:
            DataFrame: A Pandas DataFrame.
        """
        with warnings.catch_warnings(record=True):
            warnings.simplefilter('always')
            data: gspread.Worksheet = gspread.authorize(
                self.connection
            ).open_by_key(
                gsheet_id if gsheet_id
                else self.gsheet_id
            ).worksheet(sheet_name)

        # default index 0 jadi kolom
        return DataFrame(data.get_all_records())

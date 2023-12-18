#!/usr/bin/env python3

# Copyright (c) Free Software Foundation, Inc. All rights reserved.
# Licensed under the AGPL-3.0-only License. See LICENSE in the project root
# for license information.

"""test_gsheet."""

import csv
from os import path
from unittest.mock import patch

from . import (
    CONFIG_JSON,
    CONFIG_YAML,
    DataFrameTestCase,
    PATH,
    PATH_CONFIG_JSON,
    PATH_CONFIG_YAML
)
from datasae.converter.gsheet import GSheet


class MockCreds:
    """MockCreds."""

    def __init__(self, filename, **kwargs):
        """__init__."""
        pass

    @property
    def project_id(self):
        """project_id."""
        pass


class GSheetTest(DataFrameTestCase):
    """GSheetTest."""

    def __init__(self, methodName: str = 'runTest'):
        """__init__."""
        super().__init__(methodName)
        self.NAME: str = 'test_gsheet'
        self.gsheet = CONFIG_JSON(self.NAME)

    def test_config(self):
        """test_config."""
        for path_file, config in (
            (PATH_CONFIG_JSON, CONFIG_JSON),
            (PATH_CONFIG_YAML, CONFIG_YAML)
        ):
            gsheet = config(self.NAME)
            self.assertTrue(
                isinstance(gsheet, GSheet)
            )
            self.assertEqual(gsheet.name, self.NAME)
            self.assertEqual(gsheet.file_path, path_file)
            self.assertEqual(
                gsheet.client_secret_file, path.join(PATH, 'creds.json')
            )

    @patch(
        'google.oauth2.service_account.Credentials.from_service_account_file',
        side_effect=MockCreds
    )
    def test_connection(self, _):
        """test_connection."""
        self.assertTrue(hasattr(self.gsheet.connection, 'project_id'))

    @patch('gspread.authorize')
    @patch(
        'google.oauth2.service_account.Credentials.from_service_account_file',
        side_effect=MockCreds
    )
    def test_convert(self, _, mock_gspread):
        """test_convert."""
        mock_open_by_key = mock_gspread.return_value.open_by_key.return_value
        mock_worksheet = mock_open_by_key.worksheet.return_value

        with open(path.join(PATH, 'data.csv')) as file:
            mock_worksheet.get_all_records.return_value = [
                {
                    key: value
                    for key, value in row.items()
                    if key
                }
                for row in csv.DictReader(file)
            ]

        self.assertEqual(self.DATA, self.gsheet('Sheet1'))
        self.assertEqual(self.DATA, self.gsheet('Sheet1', 'gsheet_id'))

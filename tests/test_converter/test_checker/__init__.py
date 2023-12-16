#!/usr/bin/env python3

# Copyright (c) Free Software Foundation, Inc. All rights reserved.
# Licensed under the AGPL-3.0-only License. See LICENSE in the project root
# for license information.

"""test_checker."""

import csv
import json
from os import path
from unittest.mock import patch

from .. import CONFIG_JSON, CONFIG_YAML, DataFrameTestCase, PATH
from ..test_gsheet import MockCreds
from ..test_s3 import MockResponse
from ..test_sql import MockEngine, SqlTest


class CheckerTest(DataFrameTestCase):
    """CheckerTest."""

    def __init__(self, methodName: str = "CheckerTest"):
        """__init__ method."""
        super().__init__(methodName)
        self.maxDiff = None

    @patch('pandas.read_sql_query')
    @patch('sqlalchemy.create_engine', side_effect=MockEngine)
    @patch('gspread.authorize')
    @patch(
        'google.oauth2.service_account.Credentials.from_service_account_file',
        side_effect=MockCreds
    )
    @patch('minio.Minio.get_object', side_effect=MockResponse)
    def test_checker(
        self,
        mock_get_object,
        mock_from_service_account_file,
        mock_authorize,
        mock_create_engine,
        mock_read_sql_query
    ):
        """test_checker."""
        mock_open_by_key = mock_authorize.return_value.open_by_key.return_value
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

        mock_read_sql_query.return_value = SqlTest.DATA.copy()

        with open('tests/data/checker.json') as file:
            CHECKER: dict[str, list[dict]] = json.loads(file.read())

        for config in (CONFIG_JSON, CONFIG_YAML):
            self.assertDictEqual(CHECKER, config.checker)

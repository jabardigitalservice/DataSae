#!/usr/bin/env python3

# Copyright (c) Free Software Foundation, Inc. All rights reserved.
# Licensed under the AGPL-3.0-only License. See LICENSE in the project root
# for license information.

"""test_postgresql."""

from __future__ import annotations
from dataclasses import dataclass
from os import path
from unittest.mock import patch

from pandas import DataFrame
from sqlalchemy import URL

from . import CONFIG_JSON, CONFIG_YAML, DataFrameTestCase, PATH
from datasae.converter import DataSourceType


@dataclass
class MockEngine:
    """MockEngine."""

    url: str | URL


class PostgreSQLTest(DataFrameTestCase):
    """PostgreSQLTest."""

    DATA: DataFrame = DataFrame([{'column_name': 1}])

    def __init__(self, methodName: str = 'runTest'):
        """__init__."""
        super().__init__(methodName)
        self.NAME: str = 'test_postgresql'
        self.postgresql = CONFIG_JSON(self.NAME)

    def test_config(self):
        """test_config."""
        for config in (CONFIG_JSON, CONFIG_YAML):
            postgresql = config(self.NAME)
            self.assertIs(postgresql.type, DataSourceType.POSTGRESQL)
            self.assertEqual(postgresql.username, 'postgres')
            self.assertEqual(postgresql.password, 'testpassword')
            self.assertEqual(postgresql.host, 'localhost')
            self.assertEqual(postgresql.port, 5432)
            self.assertEqual(postgresql.database, 'postgres')

    @patch('sqlalchemy.create_engine', side_effect=MockEngine)
    def test_connection(self, _):
        """test_connection."""
        self.assertTrue(hasattr(self.postgresql.connection, 'url'))

    @patch('pandas.read_sql_query')
    def test_convert(self, mock_read_sql_query):
        """test_convert."""
        mock_read_sql_query.return_value = self.DATA

        self.assertEqual(
            self.DATA,
            self.postgresql('select 1 column_name;')
        )
        self.assertEqual(
            self.DATA,
            self.postgresql(path.join(PATH, 'query.sql'))
        )

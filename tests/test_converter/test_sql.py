#!/usr/bin/env python3

# Copyright (c) Free Software Foundation, Inc. All rights reserved.
# Licensed under the AGPL-3.0-only License. See LICENSE in the project root
# for license information.

"""test_sql."""

from __future__ import annotations
from dataclasses import dataclass
from os import path
from unittest.mock import patch

from pandas import DataFrame
from sqlalchemy import URL

from . import (
    CONFIG_JSON,
    CONFIG_YAML,
    DataFrameTestCase,
    PATH,
    PATH_CONFIG_JSON,
    PATH_CONFIG_YAML
)
from datasae import Sql


@dataclass
class MockEngine:
    """MockEngine."""

    url: str | URL


class SqlTest(DataFrameTestCase):
    """SqlTest."""

    DATA: DataFrame = DataFrame([{'column_name': 1, 'another_column_name': 5}])

    @patch('pandas.read_sql_query')
    @patch('sqlalchemy.create_engine', side_effect=MockEngine)
    def test_sql(self, _, mock_read_sql_query):
        """test_sql."""
        for path_file, config in (
            (PATH_CONFIG_JSON, CONFIG_JSON),
            (PATH_CONFIG_YAML, CONFIG_YAML)
        ):
            for (
                config_name,
                drivername,
                username,
                password,
                host,
                port,
                database
            ) in (
                (
                    'test_mariadb_or_mysql',
                    'mysql+pymysql',
                    'root',
                    'testpassword',
                    'localhost',
                    3306,
                    'mysql'
                ),
                (
                    'test_postgresql',
                    'postgresql',
                    'postgres',
                    'testpassword',
                    'localhost',
                    5432,
                    'postgres'
                )
            ):
                converter = config(config_name)

                # Test Config
                self.assertTrue(
                    isinstance(converter, Sql)
                )
                self.assertEqual(converter.name, config_name)
                self.assertEqual(converter.file_path, path_file)
                self.assertEqual(converter.drivername, drivername)
                self.assertEqual(converter.username, username)
                self.assertEqual(converter.password, password)
                self.assertEqual(converter.host, host)
                self.assertEqual(converter.port, port)
                self.assertEqual(converter.database, database)

                # Test Connection
                self.assertTrue(hasattr(converter.connection, 'url'))

                # Test Convert
                mock_read_sql_query.return_value = self.DATA.copy()

                self.assertEqual(
                    self.DATA,
                    converter('select 1 column_name, 5 another_column_name;')
                )
                self.assertEqual(
                    self.DATA,
                    converter(path.join(PATH, 'query.sql'))
                )

#!/usr/bin/env python3

# Copyright (C) Free Software Foundation, Inc. All rights reserved.
# Licensed under the AGPL-3.0-only License. See LICENSE in the project root
# for license information.

"""test_local."""

from os import path

from . import (
    CONFIG_JSON,
    CONFIG_YAML,
    DataFrameTestCase,
    PATH,
    PATH_CONFIG_JSON,
    PATH_CONFIG_YAML
)
from datasae.converter.local import Local


class LocalTest(DataFrameTestCase):
    """LocalTest."""

    def __init__(self, methodName: str = 'runTest'):
        """__init__."""
        super().__init__(methodName)
        self.NAME: str = 'test_local'
        self.local = CONFIG_JSON(self.NAME)

    def test_config(self):
        """test_config."""
        for path_file, config in (
            (PATH_CONFIG_JSON, CONFIG_JSON),
            (PATH_CONFIG_YAML, CONFIG_YAML)
        ):
            local = config(self.NAME)
            self.assertTrue(
                isinstance(local, Local)
            )
            self.assertEqual(local.name, self.NAME)
            self.assertEqual(local.file_path, path_file)

    def test_convert(self):
        """test_convert."""
        self.assertEqual(
            self.DATA,
            self.local(
                path.join(PATH, 'data.csv')
            ).drop('Unnamed: 0', axis='columns')
        )
        self.assertEqual(
            self.DATA,
            self.local(
                path.join(PATH, 'data.json')
            ).sort_index()
        )
        self.assertEqual(
            self.DATA,
            self.local(
                path.join(PATH, 'data.parquet')
            )
        )
        self.assertEqual(
            self.DATA,
            self.local(
                path.join(PATH, 'data.xlsx'),
                sheet_name='Sheet1'
            ).drop('Unnamed: 0', axis='columns')
        )

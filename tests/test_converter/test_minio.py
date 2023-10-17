#!/usr/bin/env python3

# Copyright (c) Free Software Foundation, Inc. All rights reserved.
# Licensed under the AGPL-3.0-only License. See LICENSE in the project root
# for license information.

from string import ascii_lowercase
from os import path
import unittest
from unittest.mock import patch

from pandas import DataFrame

from . import CONFIG_JSON, CONFIG_YAML, PATH
from datasae.converter import DataSourceType


class MockResponse:
    def close(self): pass
    def release_conn(self): pass

    def __init__(self, bucket_name: str, object_name: str):
        with open(path.join(PATH, object_name), 'rb') as file:
            self.data: bytes = file.read()

        self.headers: dict = {
            'Content-Type': {
                'data.csv': 'text/csv',
                'data.json': 'application/json',
                'data.parquet': 'application/octet-stream',
                'data.xlsx': 'application/vnd.openxmlformats-officedocument.'
                'spreadsheetml.sheet'
            }.get(object_name)
        }


class MinioTest(unittest.TestCase):
    def __init__(self, methodName: str = 'runTest'):
        super().__init__(methodName)
        self.NAME: str = 'test_minio'
        self.minio = CONFIG_JSON(self.NAME)

    def test_config(self):
        for config in (CONFIG_JSON, CONFIG_YAML):
            minio = config(self.NAME)
            self.assertIs(minio.type, DataSourceType.MINIO)
            self.assertEqual(minio.endpoint, 'play.min.io')
            self.assertEqual(minio.access_key, 'Q3AM3UQ867SPQQA43P2F')
            self.assertEqual(
                minio.secret_key, 'zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG'
            )

    def test_connection(self):
        self.assertIsNotNone(self.minio.connection)

    @patch('minio.Minio.get_object', side_effect=MockResponse)
    def test_convert(self, _):
        BUCKET_NAME: str = 'datasae'
        DATA: dict = DataFrame({'alphabet': list(ascii_lowercase)}).to_dict()

        self.assertDictEqual(
            DATA,
            self.minio(
                BUCKET_NAME, 'data.csv'
            ).drop('Unnamed: 0', axis='columns').to_dict()
        )
        self.assertDictEqual(
            DATA,
            self.minio(BUCKET_NAME, 'data.json').sort_index().to_dict()
        )
        self.assertDictEqual(
            DATA,
            self.minio(BUCKET_NAME, 'data.parquet').to_dict()
        )
        self.assertDictEqual(
            DATA,
            self.minio(
                BUCKET_NAME, 'data.xlsx'
            ).drop('Unnamed: 0', axis='columns').to_dict()
        )

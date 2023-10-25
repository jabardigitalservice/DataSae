#!/usr/bin/env python3

# Copyright (c) Free Software Foundation, Inc. All rights reserved.
# Licensed under the AGPL-3.0-only License. See LICENSE in the project root
# for license information.

"""test_s3."""

from string import ascii_lowercase
from os import path
import unittest
from unittest.mock import patch

from pandas import DataFrame
from pandas.testing import assert_frame_equal

from . import CONFIG_JSON, CONFIG_YAML, PATH
from datasae.converter import DataSourceType


class MockResponse:
    """MockResponse."""

    def close(self):
        """close."""
        pass

    def release_conn(self):
        """release_conn."""
        pass

    def __init__(self, bucket_name: str, object_name: str):
        """__init__."""
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


class S3Test(unittest.TestCase):
    """S3Test."""

    def assertDataframeEqual(self, a, b, msg):
        """assertDataframeEqual."""
        try:
            assert_frame_equal(a, b)
        except AssertionError as e:
            raise self.failureException(msg) from e

    def setUp(self):
        """Set up method."""
        self.addTypeEqualityFunc(DataFrame, self.assertDataframeEqual)

    def __init__(self, methodName: str = 'runTest'):
        """__init__."""
        super().__init__(methodName)
        self.NAME: str = 'test_s3'
        self.s3 = CONFIG_JSON(self.NAME)

    def test_config(self):
        """test_config."""
        for config in (CONFIG_JSON, CONFIG_YAML):
            s3 = config(self.NAME)
            self.assertIs(s3.type, DataSourceType.S3)
            self.assertEqual(s3.endpoint, 'play.min.io')
            self.assertEqual(s3.access_key, 'Q3AM3UQ867SPQQA43P2F')
            self.assertEqual(
                s3.secret_key, 'zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG'
            )

    def test_connection(self):
        """test_connection."""
        self.assertTrue(hasattr(self.s3.connection, 'get_object'))

    @patch('minio.Minio.get_object', side_effect=MockResponse)
    def test_convert(self, _):
        """test_convert."""
        BUCKET_NAME: str = 'datasae'
        DATA: DataFrame = DataFrame({'alphabet': list(ascii_lowercase)})

        with self.assertRaises(AssertionError):
            self.assertEqual(DATA, DataFrame())

        self.assertEqual(
            DATA,
            self.s3(
                BUCKET_NAME, 'data.csv'
            ).drop('Unnamed: 0', axis='columns')
        )
        self.assertEqual(
            DATA,
            self.s3(BUCKET_NAME, 'data.json').sort_index()
        )
        self.assertEqual(
            DATA,
            self.s3(BUCKET_NAME, 'data.parquet')
        )
        self.assertEqual(
            DATA,
            self.s3(
                BUCKET_NAME, 'data.xlsx', sheet_name='Sheet1'
            ).drop('Unnamed: 0', axis='columns')
        )

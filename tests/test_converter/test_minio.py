#!/usr/bin/env python3

# Copyright (c) Free Software Foundation, Inc. All rights reserved.
# Licensed under the AGPL-3.0-only License. See LICENSE in the project root
# for license information.

import unittest

from datasae.converter import Config, DataSourceType, FileType


class MinioTest(unittest.TestCase):
    def __init__(self, methodName: str = 'runTest'):
        super().__init__(methodName)
        self.PATH: str = 'tests/data/config'
        self.NAME: str = 'test_minio'
        self.minio = Config(f'{self.PATH}{FileType.JSON}')(self.NAME)

    def test_config(self):
        for file_type in (FileType.JSON, FileType.YAML):
            minio = Config(f'{self.PATH}{file_type}')(self.NAME)
            self.assertIs(minio.type, DataSourceType.MINIO)
            self.assertEqual(minio.endpoint, 'play.min.io')
            self.assertEqual(minio.access_key, 'Q3AM3UQ867SPQQA43P2F')
            self.assertEqual(
                minio.secret_key, 'zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG'
            )

    def test_connection(self):
        self.assertIsNone(self.minio.connection())

    def test_read(self):
        self.assertIsNone(self.minio.read())

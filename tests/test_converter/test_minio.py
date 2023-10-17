#!/usr/bin/env python3

# Copyright (c) Free Software Foundation, Inc. All rights reserved.
# Licensed under the AGPL-3.0-only License. See LICENSE in the project root
# for license information.

import unittest

from datasae.converter import DataSourceType

from . import CONFIG_JSON, CONFIG_YAML


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

#!/usr/bin/env python3

# Copyright (c) Free Software Foundation, Inc. All rights reserved.
# Licensed under the AGPL-3.0-only License. See LICENSE in the project root
# for license information.

import unittest

from datasae.converter import Config, FileType

CONFIG_JSON: Config = Config('tests/data/config.json')
CONFIG_YAML: Config = Config('tests/data/config.yaml')


class CaseInsensitiveEnumTest(unittest.TestCase):
    def test_case_insensitive_enum(self):
        self.assertEqual('.JSON', FileType.JSON)
        self.assertIs(FileType('.JSON'), FileType.JSON)

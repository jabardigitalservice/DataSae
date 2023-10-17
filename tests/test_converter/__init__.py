#!/usr/bin/env python3

# Copyright (c) Free Software Foundation, Inc. All rights reserved.
# Licensed under the AGPL-3.0-only License. See LICENSE in the project root
# for license information.

from os import path
import unittest

from datasae.converter import Config, FileType

PATH: str = path.join('tests', 'data')
CONFIG_JSON: Config = Config(path.join(PATH, 'config.json'))
CONFIG_YAML: Config = Config(path.join(PATH, 'config.yaml'))


class CaseInsensitiveEnumTest(unittest.TestCase):
    def test_case_insensitive_enum(self):
        self.assertEqual('.JSON', FileType.JSON)
        self.assertIs(FileType('.JSON'), FileType.JSON)

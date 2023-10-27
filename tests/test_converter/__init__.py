#!/usr/bin/env python3

# Copyright (c) Free Software Foundation, Inc. All rights reserved.
# Licensed under the AGPL-3.0-only License. See LICENSE in the project root
# for license information.

"""test_converter."""

from os import path
import unittest

from pandas import DataFrame
from pandas.testing import assert_frame_equal

from datasae.converter import Config, FileType

PATH: str = path.join('tests', 'data')
CONFIG_JSON: Config = Config(path.join(PATH, 'config.json'))
CONFIG_YAML: Config = Config(path.join(PATH, 'config.yaml'))


class CaseInsensitiveEnumTest(unittest.TestCase):
    """CaseInsensitiveEnumTest."""

    def test_case_insensitive_enum(self):
        """test_case_insensitive_enum."""
        self.assertEqual('.JSON', FileType.JSON)
        self.assertIs(FileType('.JSON'), FileType.JSON)


class DataFrameTestCase(unittest.TestCase):
    """DataFrameTestCase."""

    def assertDataframeEqual(self, a, b, msg):
        """assertDataframeEqual."""
        try:
            assert_frame_equal(a, b)
        except AssertionError as e:
            raise self.failureException(msg) from e

    def setUp(self):
        """Set up method."""
        self.addTypeEqualityFunc(DataFrame, self.assertDataframeEqual)

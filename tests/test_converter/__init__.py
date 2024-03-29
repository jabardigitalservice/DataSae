#!/usr/bin/env python3

# Copyright (C) Free Software Foundation, Inc. All rights reserved.
# Licensed under the AGPL-3.0-only License. See LICENSE in the project root
# for license information.

"""test_converter."""

from os import path
from string import ascii_lowercase, ascii_uppercase
import unittest

from pandas import DataFrame
from pandas.testing import assert_frame_equal

from datasae.converter import Config, FileType

PATH: str = path.join('tests', 'data')
PATH_CONFIG_JSON: str = path.join(PATH, 'config.json')
PATH_CONFIG_YAML: str = path.join(PATH, 'config.yaml')
CONFIG_JSON: Config = Config(PATH_CONFIG_JSON)
CONFIG_YAML: Config = Config(PATH_CONFIG_YAML)


class CaseInsensitiveEnumTest(unittest.TestCase):
    """CaseInsensitiveEnumTest."""

    def test_case_insensitive_enum(self):
        """test_case_insensitive_enum."""
        self.assertEqual('.JSON', FileType.JSON)
        self.assertIs(FileType('.JSON'), FileType.JSON)


class DataFrameTestCase(unittest.TestCase):
    """DataFrameTestCase."""

    DATA: DataFrame = DataFrame({
        'alphabet': list(ascii_lowercase),
        'ALPHABET': list(ascii_uppercase)
    })

    def assertDataframeEqual(self, a, b, msg):
        """assertDataframeEqual."""
        try:
            assert_frame_equal(a, b)
        except AssertionError as e:
            raise self.failureException(msg) from e

    def setUp(self):
        """Set up method."""
        self.addTypeEqualityFunc(DataFrame, self.assertDataframeEqual)

    def test_assertion_error(self):
        """test_assertion_error."""
        with self.assertRaises(AssertionError):
            self.assertEqual(DataFrame({'a': [1]}), DataFrame())

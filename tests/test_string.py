#!/usr/bin/env python3

# Copyright (C) Free Software Foundation, Inc. All rights reserved.
# Licensed under the AGPL-3.0-only License. See LICENSE in the project root
# for license information.

"""test_string."""

import unittest

import pandas as pd

from . import MESSAGE
from datasae.string import String, WarningDataDetailMessage
from datasae.utils import create_warning_data, WarningDataMessage


class StringTest(unittest.TestCase):
    """StringTest."""

    def __init__(self, methodName: str = "TestString"):
        """__init__."""
        super().__init__(methodName)
        self.maxDiff = None

    def test_contain_valid(self):
        """test_contain_valid."""
        dummy = pd.DataFrame(
            {
                "column": [
                    "Python",
                    "Python",
                    "Python",
                    "Python",
                    "Python",
                    "Python",
                    "Python",
                    "Python",
                    "Python",
                    "Python",
                ]
            }
        )

        actual_result = String(dummy).contain("Python", "column")
        expected_result = {
            "score": 1.0,
            "valid": 10,
            "invalid": 0,
            "warning": {},
        }

        self.assertDictEqual(actual_result, expected_result, MESSAGE)

    def test_contain_invalid(self):
        """test_contain_invalid."""
        dummy = pd.DataFrame(
            {"column": ["Python", "PYTHON", "Bukan", 42, 3.14]}
        )

        actual_result = String(dummy).contain("Python", "column")
        expected_result = {
            "score": 0.2,
            "valid": 1,
            "invalid": 4,
            "warning": {
                1: create_warning_data(
                    "PYTHON", "Value should be contain to Python"
                ),
                2: create_warning_data(
                    "Bukan", "Value should be contain to Python"
                ),
                3: create_warning_data(
                    42,
                    WarningDataDetailMessage.STRING_DATA_TYPE,
                    WarningDataMessage.INVALID_DATA_TYPE,
                ),
                4: create_warning_data(
                    3.14,
                    WarningDataDetailMessage.STRING_DATA_TYPE,
                    WarningDataMessage.INVALID_DATA_TYPE,
                ),
            },
        }

        self.assertDictEqual(actual_result, expected_result, MESSAGE)

    def test_not_contain_valid(self):
        """test_not_contain_valid."""
        dummy = pd.DataFrame(
            {"column": ["python", "PYTHON", "Bukan", "Ini String", "String"]}
        )

        actual_result = String(dummy).not_contain("Python", "column")
        expected_result = {
            "score": 1.0,
            "valid": 5,
            "invalid": 0,
            "warning": {},
        }

        self.assertDictEqual(actual_result, expected_result, MESSAGE)

    def test_not_contain_invalid(self):
        """test_not_contain_invalid."""
        dummy = pd.DataFrame(
            {"column": ["Python", "python", "PYTHON", 42, 3.14]}
        )

        actual_result = String(dummy).not_contain("Python", "column")
        expected_result = {
            "score": 0.4,
            "valid": 2,
            "invalid": 3,
            "warning": {
                0: create_warning_data(
                    "Python", "Value should be not contain to Python"
                ),
                3: create_warning_data(
                    42,
                    WarningDataDetailMessage.STRING_DATA_TYPE,
                    WarningDataMessage.INVALID_DATA_TYPE,
                ),
                4: create_warning_data(
                    3.14,
                    WarningDataDetailMessage.STRING_DATA_TYPE,
                    WarningDataMessage.INVALID_DATA_TYPE,
                ),
            },
        }

        self.assertDictEqual(actual_result, expected_result, MESSAGE)

    def test_regex_custom_valid(self):
        """test_regex_custom_valid."""
        dummy = pd.DataFrame(
            {
                "column": [
                    "Python",
                    "Ini Python",
                    "Belajar Python",
                    "Python",
                    "Itu Python",
                ]
            }
        )

        actual_result = String(dummy).regex_contain(
            "Python", "column"
        )
        expected_result = {
            "score": 1.0,
            "valid": 5,
            "invalid": 0,
            "warning": {},
        }

        self.assertDictEqual(actual_result, expected_result, MESSAGE)

    def test_regex_custom_invalid(self):
        """test_regex_custom_invalid."""
        dummy = pd.DataFrame(
            {"column": ["Python", "Ini Python", "bukan python", 77, 3.17]}
        )

        actual_result = String(dummy).regex_contain(
            "Python", "column"
        )
        expected_result = {
            "score": 0.4,
            "valid": 2,
            "invalid": 3,
            "warning": {
                2: create_warning_data(
                    "bukan python", "Value should be contain to Python"
                ),
                3: create_warning_data(
                    77,
                    WarningDataDetailMessage.STRING_DATA_TYPE,
                    WarningDataMessage.INVALID_DATA_TYPE,
                ),
                4: create_warning_data(
                    3.17,
                    WarningDataDetailMessage.STRING_DATA_TYPE,
                    WarningDataMessage.INVALID_DATA_TYPE,
                ),
            },
        }

        self.assertDictEqual(actual_result, expected_result, MESSAGE)

    def test_special_character_valid(self):
        """test_special_character_valid."""
        dummy = pd.DataFrame(
            {"column": ["Python !", "! Python", "!python", "!", "!!"]}
        )

        actual_result = String(dummy).special_char_contain(
            "!", "column"
        )
        expected_result = {
            "score": 1.0,
            "valid": 5,
            "invalid": 0,
            "warning": {},
        }

        self.assertDictEqual(actual_result, expected_result, MESSAGE)

    def test_special_character_invalid(self):
        """test_special_character_invalid."""
        dummy = pd.DataFrame({"column": ["!", "? Python", "!python", 3, 3.14]})

        actual_result = String(dummy).special_char_contain(
            "!", "column"
        )
        expected_result = {
            "score": 0.4,
            "valid": 2,
            "invalid": 3,
            "warning": {
                1: create_warning_data(
                    "? Python", "Value should be contain to !"
                ),
                3: create_warning_data(
                    3,
                    WarningDataDetailMessage.STRING_DATA_TYPE,
                    WarningDataMessage.INVALID_DATA_TYPE,
                ),
                4: create_warning_data(
                    3.14,
                    WarningDataDetailMessage.STRING_DATA_TYPE,
                    WarningDataMessage.INVALID_DATA_TYPE,
                ),
            },
        }

        self.assertDictEqual(actual_result, expected_result, MESSAGE)

    # def test_length(self):
    #    dummy = pd.DataFrame(
    #        {
    #            "column": ["Python", "Ini Python", "Belajar python",
    #                       "Suka Python", "Python"]
    #            }
    #        )

    #    actual_result = String(dummy).length("column")
    #    expected_result = pd.DataFrame(
    #        {
    #            'column': ['Python', 'Ini Python', 'Belajar python',
    #                       'Suka Python', 'Python'],
    #            'df_length_column': [6, 10, 14, 11, 6]
    #            }
    #        )

    #    self.assertDictEqual(actual_result, expected_result, MESSAGE)

    # def test_word_count(self):
    #    dummy = pd.DataFrame(
    #        {
    #            "column": ["Python", "Ini Python", "Belajar python",
    #                       "Suka Python", "Python"]
    #            }
    #        )

    #    actual_result = String(dummy).word_count("column")
    #    expected_result = pd.DataFrame(
    #        {
    #            'column': ['Python', 'Ini Python', 'Belajar python',
    #                       'Suka Python', 'Python'],
    #            'df_word_count_column': [1, 2, 2, 2, 1]
    #            }
    #        )

    #    self.assertDictEqual(actual_result, expected_result, MESSAGE)

    def test_lowercase_valid(self):
        """test_lowercase_valid."""
        dummy = pd.DataFrame(
            {
                "column": [
                    "python",
                    "ini python",
                    "belajar python",
                    "suka python",
                    "python",
                ]
            }
        )

        actual_result = String(dummy).is_lowercase("column")
        expected_result = {
            "score": 1.0,
            "valid": 5,
            "invalid": 0,
            "warning": {},
        }

        self.assertDictEqual(actual_result, expected_result, MESSAGE)

    def test_lowercase_invalid(self):
        """test_lowercase_invalid."""
        dummy = pd.DataFrame(
            {"column": ["python", "ini Python", 3.14, 3, "python"]}
        )

        actual_result = String(dummy).is_lowercase("column")
        expected_result = {
            "score": 0.4,
            "valid": 2,
            "invalid": 3,
            "warning": {
                1: create_warning_data("ini Python", "Value should lowercase"),
                2: create_warning_data(
                    3.14,
                    WarningDataDetailMessage.STRING_DATA_TYPE,
                    WarningDataMessage.INVALID_DATA_TYPE,
                ),
                3: create_warning_data(
                    3,
                    WarningDataDetailMessage.STRING_DATA_TYPE,
                    WarningDataMessage.INVALID_DATA_TYPE,
                ),
            },
        }

        self.assertDictEqual(actual_result, expected_result, MESSAGE)

    def test_uppercase_valid(self):
        """test_uppercase_valid."""
        dummy = pd.DataFrame(
            {"column": ["PYTHON", "INI", "PYTHON", "SUKA", "PYTHON"]}
        )

        actual_result = String(dummy).is_uppercase("column")
        expected_result = {
            "score": 1.0,
            "valid": 5,
            "invalid": 0,
            "warning": {},
        }

        self.assertDictEqual(actual_result, expected_result, MESSAGE)

    def test_uppercase_invalid(self):
        """test_uppercase_invalid."""
        dummy = pd.DataFrame({"column": ["PYTHON", "Ini", 3.14, 3, "PYTHON"]})

        actual_result = String(dummy).is_uppercase("column")
        expected_result = {
            "score": 0.4,
            "valid": 2,
            "invalid": 3,
            "warning": {
                1: create_warning_data("Ini", "Value should uppercase"),
                2: create_warning_data(
                    3.14,
                    WarningDataDetailMessage.STRING_DATA_TYPE,
                    WarningDataMessage.INVALID_DATA_TYPE,
                ),
                3: create_warning_data(
                    3,
                    WarningDataDetailMessage.STRING_DATA_TYPE,
                    WarningDataMessage.INVALID_DATA_TYPE,
                ),
            },
        }

        self.assertDictEqual(actual_result, expected_result, MESSAGE)

    def test_capitalise_first_word_valid(self):
        """test_capitalise_first_word_valid."""
        dummy = pd.DataFrame(
            {"column": ["Python", "Ini saya", "Python", "Suka", "Python"]}
        )

        actual_result = String(dummy).is_capitalize_first_word(
            "column"
        )
        expected_result = {
            "score": 1.0,
            "valid": 5,
            "invalid": 0,
            "warning": {},
        }

        self.assertDictEqual(actual_result, expected_result, MESSAGE)

    def test_capitalise_first_word_invalid(self):
        """test_capitalise_first_word_invalid."""
        dummy = pd.DataFrame(
            {"column": ["Python", "ini saya", 3.14, 3, "Python"]}
        )

        actual_result = String(dummy).is_capitalize_first_word(
            "column"
        )
        expected_result = {
            "score": 0.4,
            "valid": 2,
            "invalid": 3,
            "warning": {
                1: create_warning_data(
                    "ini saya", "Value should capitalize first word"
                ),
                2: create_warning_data(
                    3.14,
                    WarningDataDetailMessage.STRING_DATA_TYPE,
                    WarningDataMessage.INVALID_DATA_TYPE,
                ),
                3: create_warning_data(
                    3,
                    WarningDataDetailMessage.STRING_DATA_TYPE,
                    WarningDataMessage.INVALID_DATA_TYPE,
                ),
            },
        }

        self.assertDictEqual(actual_result, expected_result, MESSAGE)

    def test_capitalise_all_word_valid(self):
        """test_capitalise_all_word_valid."""
        dummy = pd.DataFrame(
            {
                "column": [
                    "Python",
                    "Ini Saya",
                    "Aku Belajar Python",
                    "Suka",
                    "Python",
                ]
            }
        )

        actual_result = String(dummy).is_capitalize_all_word(
            "column"
        )
        expected_result = {
            "score": 1.0,
            "valid": 5,
            "invalid": 0,
            "warning": {},
        }

        self.assertDictEqual(actual_result, expected_result, MESSAGE)

    def test_capitalise_all_word_invalid(self):
        """test_capitalise_all_word_invalid."""
        dummy = pd.DataFrame(
            {"column": ["Python", "ini saya", 3.14, 3, "Belajar Python"]}
        )

        actual_result = String(dummy).is_capitalize_all_word(
            "column"
        )
        expected_result = {
            "score": 0.4,
            "valid": 2,
            "invalid": 3,
            "warning": {
                1: create_warning_data(
                    "ini saya", "Value should capitalize all word"
                ),
                2: create_warning_data(
                    3.14,
                    WarningDataDetailMessage.STRING_DATA_TYPE,
                    WarningDataMessage.INVALID_DATA_TYPE,
                ),
                3: create_warning_data(
                    3,
                    WarningDataDetailMessage.STRING_DATA_TYPE,
                    WarningDataMessage.INVALID_DATA_TYPE,
                ),
            },
        }

        self.assertDictEqual(actual_result, expected_result, MESSAGE)

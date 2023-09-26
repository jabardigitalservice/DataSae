#!/usr/bin/env python3

# This module is part of DataSae and is released under
# the AGPL-3.0-only License: https://opensource.org/license/agpl-v3/

import unittest

import pandas as pd

from datasae.string import String, WarningDataDetailMessage
from datasae.utils import create_warning_data, WarningDataMessage

from . import MESSAGE


class StringTest(unittest.TestCase):
    def __init__(self, methodName: str = "TestString"):
        super().__init__(methodName)
        self.maxDiff = None

    def test_contain_valid(self):
        dummy = pd.DataFrame(
            {
                "column": ["Python", "Python", "Python", "Python", "Python",
                           "Python", "Python", "Python", "Python", "Python"]
                }
            )

        actual_result = String(dummy).df_column_contain("Python", "column")
        expected_result = {
            "score": 1.0,
            "valid": 10,
            "invalid": 0,
            "warning": {},
        }

        self.assertDictEqual(actual_result, expected_result, MESSAGE)

    def test_contain_invalid(self):
        dummy = pd.DataFrame(
            {
                "column": ["Python", "PYTHON", "Bukan", 42, 3.14]
            }
        )

        actual_result = String(dummy).df_column_contain("Python", "column")
        expected_result = {
            "score": 0.2,
            "valid": 1,
            "invalid": 4,
            "warning": {
                1: create_warning_data(
                    "PYTHON",
                    "Value should be contain to Python"
                ),
                2: create_warning_data(
                    "Bukan",
                    "Value should be contain to Python"
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
        dummy = pd.DataFrame(
            {
                "column": ["python", "PYTHON", "Bukan", "Ini String", "String"]
                }
            )

        actual_result = String(dummy).df_column_not_contain("Python", "column")
        expected_result = {
            "score": 1.0,
            "valid": 5,
            "invalid": 0,
            "warning": {},
        }

        self.assertDictEqual(actual_result, expected_result, MESSAGE)

    def test_not_contain_invalid(self):
        dummy = pd.DataFrame(
            {
                "column": ["Python", "python", "PYTHON", 42, 3.14]
            }
        )

        actual_result = String(dummy).df_column_not_contain("Python", "column")
        expected_result = {
            "score": 0.4,
            "valid": 2,
            "invalid": 3,
            "warning": {
                0: create_warning_data(
                    "Python",
                    "Value should be not contain to Python"
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

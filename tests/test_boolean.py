#!/usr/bin/env python3

# This module is part of DataSae and is released under
# the AGPL-3.0-only License: https://opensource.org/license/agpl-v3/

import random
import unittest

import pandas as pd

from . import MESSAGE
from datasae.boolean import Boolean, WarningDataDetailMessage
from datasae.utils import create_warning_data, WarningDataMessage


class BooleanTest(unittest.TestCase):
    def __init__(self, methodName: str = "BooleanTest"):
        super().__init__(methodName)
        self.maxDiff = None

    def test_is_bool_valid(self):
        dummy = pd.DataFrame(
            {"columm": [random.choice([True, False]) for i in range(25)]}
        )

        actual_result = Boolean(dummy).is_bool("columm")
        excepted_result = {
            "score": 1.0,
            "valid": 25,
            "invalid": 0,
            "warning": {},
        }

        self.assertDictEqual(actual_result, excepted_result, MESSAGE)

    def test_is_bool_invalid(self):
        dummy = pd.concat(
            [
                pd.DataFrame(
                    {
                        "columm": [
                            random.choice([True, False]) for i in range(25)
                        ]
                    }
                ),
                pd.DataFrame(
                    [
                        {"columm": None},
                        {"columm": 1},
                        {"columm": "True"},
                    ]
                ),
            ]
        ).reset_index(drop=True)

        actual_result = Boolean(dummy).is_bool("columm")

        excepted_result = {
            "score": 0.8928571428571429,
            "valid": 25,
            "invalid": 3,
            "warning": {
                25: create_warning_data(
                    None,
                    WarningDataDetailMessage.BOOLEAN_DATA_TYPE,
                    WarningDataMessage.INVALID_DATA_TYPE,
                ),
                26: create_warning_data(
                    1,
                    WarningDataDetailMessage.BOOLEAN_DATA_TYPE,
                    WarningDataMessage.INVALID_DATA_TYPE,
                ),
                27: create_warning_data(
                    "True",
                    WarningDataDetailMessage.BOOLEAN_DATA_TYPE,
                    WarningDataMessage.INVALID_DATA_TYPE,
                ),
            },
        }

        self.assertDictEqual(actual_result, excepted_result, MESSAGE)

    def test_check_is_in_valid(self):
        dummy = pd.DataFrame(
            {"columm": [random.choice(["true", "false"]) for i in range(25)]}
        )

        actual_result = Boolean(dummy).is_in(["true", "false"], "columm")
        excepted_result = {
            "score": 1.0,
            "valid": 25,
            "invalid": 0,
            "warning": {},
        }

        self.assertDictEqual(actual_result, excepted_result, MESSAGE)

    def test_check_is_in_invalid(self):
        dummy = pd.concat(
            [
                pd.DataFrame(
                    {
                        "columm": [
                            random.choice(["true", "false"]) for i in range(25)
                        ]
                    }
                ),
                pd.DataFrame(
                    [
                        {"columm": None},
                        {"columm": 1},
                        {"columm": "True"},
                    ]
                ),
            ]
        ).reset_index(drop=True)

        actual_result = Boolean(dummy).is_in(["true", "false"], "columm")
        excepted_result = {
            "score": 0.8928571428571429,
            "valid": 25,
            "invalid": 3,
            "warning": {
                    25: create_warning_data(
                        None,
                        WarningDataDetailMessage.DEFINED_DATA_TYPE,
                        WarningDataMessage.INVALID_DATA_TYPE,
                    ),
                    26: create_warning_data(
                        1,
                        WarningDataDetailMessage.DEFINED_DATA_TYPE,
                        WarningDataMessage.INVALID_DATA_TYPE,
                    ),
                    27: create_warning_data(
                        "True",
                        WarningDataDetailMessage.DEFINED_DATA_TYPE,
                        WarningDataMessage.INVALID_DATA_TYPE,
                    ),
                },
            }

        self.assertDictEqual(actual_result, excepted_result, MESSAGE)

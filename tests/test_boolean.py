#!/usr/bin/env python3

# Copyright (C) Free Software Foundation, Inc. All rights reserved.
# Licensed under the AGPL-3.0-only License. See LICENSE in the project root
# for license information.

"""test_boolean library."""

import random
import unittest

import pandas as pd

from . import MESSAGE
from datasae.boolean import Boolean, WarningDataDetailMessage
from datasae.utils import create_warning_data, WarningDataMessage


class BooleanTest(unittest.TestCase):
    """BooleanTest class."""

    def __init__(self, methodName: str = "BooleanTest"):
        """__init__ method."""
        super().__init__(methodName)
        self.maxDiff = None

    def test_is_bool_valid(self):
        """test_is_bool_valid method."""
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
        """test_is_bool_invalid method."""
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
        """test_check_is_in_valid method."""
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
        """test_check_is_in_invalid method."""
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

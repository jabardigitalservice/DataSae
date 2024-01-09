#!/usr/bin/env python3

# Copyright (C) Free Software Foundation, Inc. All rights reserved.
# Licensed under the AGPL-3.0-only License. See LICENSE in the project root
# for license information.

"""test_integer."""

import unittest

import numpy as np
import pandas as pd

from datasae.integer import Integer, WarningDataDetailMessage
from datasae.utils import create_warning_data, WarningDataMessage

from . import MESSAGE


class IntegerTest(unittest.TestCase):
    """IntegerTest."""

    def __init__(self, methodName: str = "TestInteger"):
        """__init__."""
        super().__init__(methodName)
        self.maxDiff = None

    def test_equal_to_valid(self):
        """test_equal_to_valid."""
        dummy = pd.DataFrame({"columm": [11 for i in range(25)]})

        actual_result = Integer(dummy).equal_to(11, "columm")
        excepted_result = {
            "score": 1.0,
            "valid": 25,
            "invalid": 0,
            "warning": {},
        }

        self.assertDictEqual(actual_result, excepted_result, MESSAGE)

    def test_equal_to_invalid(self):
        """test_equal_to_invalid."""
        dummy = pd.concat(
            [
                pd.DataFrame({"columm": [11 for i in range(25)]}),
                pd.DataFrame(
                    [
                        {"columm": "11"},
                        {"columm": 44},
                        {"columm": 10.2},
                    ]
                ),
            ]
        )

        actual_result = Integer(dummy).equal_to(11, "columm")
        excepted_result = {
            "score": 0.8928571428571429,
            "valid": 25,
            "invalid": 3,
            "warning": {
                25: create_warning_data(
                    "11",
                    WarningDataDetailMessage.INTEGER_DATA_TYPE,
                    WarningDataMessage.INVALID_DATA_TYPE,
                ),
                26: create_warning_data(44, "Value should be equal to 11"),
                27: create_warning_data(
                    10.2,
                    WarningDataDetailMessage.INTEGER_DATA_TYPE,
                    WarningDataMessage.INVALID_DATA_TYPE,
                ),
            },
        }

        self.assertDictEqual(actual_result, excepted_result, MESSAGE)

    def test_less_valid(self):
        """test_less_valid."""
        dummy = pd.DataFrame({"columm": np.random.randint(0, 10, 25)})

        actual_result = Integer(dummy).less_than(11, "columm")
        excepted_result = {
            "score": 1.0,
            "valid": 25,
            "invalid": 0,
            "warning": {},
        }

        self.assertDictEqual(actual_result, excepted_result, MESSAGE)

    def test_less_invalid(self):
        """test_less_invalid."""
        dummy = pd.concat(
            [
                pd.DataFrame({"columm": np.random.randint(0, 10, 20)}),
                pd.DataFrame(
                    [
                        {"columm": "11"},
                        {"columm": 44},
                        {"columm": 10.2},
                        {"columm": -1},
                    ]
                ),
            ]
        )

        actual_result = Integer(dummy).less_than(10, "columm")
        excepted_result = {
            "score": 0.875,
            "valid": 21,
            "invalid": 3,
            "warning": {
                20: create_warning_data(
                    "11",
                    WarningDataDetailMessage.INTEGER_DATA_TYPE,
                    WarningDataMessage.INVALID_DATA_TYPE,
                ),
                21: create_warning_data(44, "Value should be less than 10"),
                22: create_warning_data(
                    10.2,
                    WarningDataDetailMessage.INTEGER_DATA_TYPE,
                    WarningDataMessage.INVALID_DATA_TYPE,
                ),
            },
        }

        self.assertDictEqual(actual_result, excepted_result, MESSAGE)

    def test_less_equal_valid(self):
        """test_less_equal_valid."""
        dummy = pd.DataFrame({"columm": np.random.randint(0, 10, 25)})

        actual_result = Integer(dummy).less_than_equal(10, "columm")
        excepted_result = {
            "score": 1.0,
            "valid": 25,
            "invalid": 0,
            "warning": {},
        }

        self.assertDictEqual(actual_result, excepted_result, MESSAGE)

    def test_less_equal_invalid(self):
        """test_less_equal_invalid."""
        dummy = pd.concat(
            [
                pd.DataFrame({"columm": np.random.randint(0, 10, 20)}),
                pd.DataFrame(
                    [
                        {"columm": "11"},
                        {"columm": 44},
                        {"columm": 11.2},
                        {"columm": -1},
                    ]
                ),
            ]
        )

        actual_result = Integer(dummy).less_than_equal(10, "columm")
        excepted_result = {
            "score": 0.875,
            "valid": 21,
            "invalid": 3,
            "warning": {
                20: create_warning_data(
                    "11",
                    WarningDataDetailMessage.INTEGER_DATA_TYPE,
                    WarningDataMessage.INVALID_DATA_TYPE,
                ),
                21: create_warning_data(
                    44, "Value should be less than equal 10"
                ),
                22: create_warning_data(
                    11.2,
                    WarningDataDetailMessage.INTEGER_DATA_TYPE,
                    WarningDataMessage.INVALID_DATA_TYPE,
                ),
            },
        }

        self.assertDictEqual(actual_result, excepted_result, MESSAGE)

    def test_greater_valid(self):
        """test_greater_valid."""
        dummy = pd.DataFrame({"columm": np.random.randint(10, 20, 25)})

        actual_result = Integer(dummy).greater_than(9, "columm")
        excepted_result = {
            "score": 1.0,
            "valid": 25,
            "invalid": 0,
            "warning": {},
        }

        self.assertDictEqual(actual_result, excepted_result, MESSAGE)

    def test_greater_invalid(self):
        """test_greater_invalid."""
        dummy = pd.concat(
            [
                pd.DataFrame({"columm": np.random.randint(11, 20, 20)}),
                pd.DataFrame(
                    [
                        {"columm": "11"},
                        {"columm": 9},
                        {"columm": 9.2},
                        {"columm": 11},
                    ]
                ),
            ]
        )

        actual_result = Integer(dummy).greater_than(10, "columm")
        excepted_result = {
            "score": 0.875,
            "valid": 21,
            "invalid": 3,
            "warning": {
                20: create_warning_data(
                    "11",
                    WarningDataDetailMessage.INTEGER_DATA_TYPE,
                    WarningDataMessage.INVALID_DATA_TYPE,
                ),
                21: create_warning_data(9, "Value should be greater than 10"),
                22: create_warning_data(
                    9.2,
                    WarningDataDetailMessage.INTEGER_DATA_TYPE,
                    WarningDataMessage.INVALID_DATA_TYPE,
                ),
            },
        }

        self.assertDictEqual(actual_result, excepted_result, MESSAGE)

    def test_greater_equal_valid(self):
        """test_greater_equal_valid."""
        dummy = pd.DataFrame({"columm": np.random.randint(10, 20, 25)})

        actual_result = Integer(dummy).greater_than_equal(10, "columm")
        excepted_result = {
            "score": 1.0,
            "valid": 25,
            "invalid": 0,
            "warning": {},
        }

        self.assertDictEqual(actual_result, excepted_result, MESSAGE)

    def test_greater_equal_invalid(self):
        """test_greater_equal_invalid."""
        dummy = pd.concat(
            [
                pd.DataFrame({"columm": np.random.randint(10, 20, 20)}),
                pd.DataFrame(
                    [
                        {"columm": "11"},
                        {"columm": 9},
                        {"columm": 9.2},
                        {"columm": 10},
                    ]
                ),
            ]
        )

        actual_result = Integer(dummy).greater_than_equal(10, "columm")
        excepted_result = {
            "score": 0.875,
            "valid": 21,
            "invalid": 3,
            "warning": {
                20: create_warning_data(
                    "11",
                    WarningDataDetailMessage.INTEGER_DATA_TYPE,
                    WarningDataMessage.INVALID_DATA_TYPE,
                ),
                21: create_warning_data(
                    9, "Value should be greater than equal 10"
                ),
                22: create_warning_data(
                    9.2,
                    WarningDataDetailMessage.INTEGER_DATA_TYPE,
                    WarningDataMessage.INVALID_DATA_TYPE,
                ),
            },
        }

        self.assertDictEqual(actual_result, excepted_result, MESSAGE)

    def test_in_range_valid(self):
        """test_in_range_valid."""
        dummy = pd.DataFrame({"columm": np.random.randint(0, 10, 25)})

        actual_result = Integer(dummy).in_range(-2, 11, "columm")
        excepted_result = {
            "score": 1.0,
            "valid": 25,
            "invalid": 0,
            "warning": {},
        }

        self.assertDictEqual(actual_result, excepted_result, MESSAGE)

    def test_in_range_invalid(self):
        """test_in_range_invalid."""
        dummy = pd.concat(
            [
                pd.DataFrame({"columm": np.random.randint(0, 10, 25)}),
                pd.DataFrame(
                    [{"columm": -5}, {"columm": 44}, {"columm": "0"}]
                ),
            ]
        )

        actual_result = Integer(dummy).in_range(-2, 11, "columm")
        excepted_result = {
            "score": 0.8928571428571429,
            "valid": 25,
            "invalid": 3,
            "warning": {
                25: create_warning_data(
                    -5, "Value should be in the range of -2 and 11"
                ),
                26: create_warning_data(
                    44, "Value should be in the range of -2 and 11"
                ),
                27: create_warning_data(
                    "0",
                    WarningDataDetailMessage.INTEGER_DATA_TYPE,
                    WarningDataMessage.INVALID_DATA_TYPE,
                ),
            },
        }

        self.assertDictEqual(actual_result, excepted_result, MESSAGE)

    def test_is_in_valid(self):
        """test_is_in_valid."""
        dummy = pd.DataFrame({"columm": np.random.randint(0, 10, 25)})

        actual_result = Integer(dummy).is_in(range(10), "columm")
        excepted_result = {
            "score": 1.0,
            "valid": 25,
            "invalid": 0,
            "warning": {},
        }

        self.assertDictEqual(actual_result, excepted_result, MESSAGE)

    def test_is_in_invalid(self):
        """test_is_in_invalid."""
        dummy = pd.concat(
            [
                pd.DataFrame({"columm": np.random.randint(0, 10, 25)}),
                pd.DataFrame(
                    [{"columm": -5}, {"columm": 44}, {"columm": "0"}]
                ),
            ]
        )

        actual_result = Integer(dummy).is_in(range(10), "columm")
        excepted_result = {
            "score": 0.8928571428571429,
            "valid": 25,
            "invalid": 3,
            "warning": {
                25: create_warning_data(-5, "Value should be in range(0, 10)"),
                26: create_warning_data(44, "Value should be in range(0, 10)"),
                27: create_warning_data(
                    "0",
                    WarningDataDetailMessage.INTEGER_DATA_TYPE,
                    WarningDataMessage.INVALID_DATA_TYPE,
                ),
            },
        }

        self.assertDictEqual(actual_result, excepted_result, MESSAGE)

    def test_not_in_valid(self):
        """test_not_in_valid."""
        dummy = pd.DataFrame({"columm": np.random.randint(0, 10, 25)})

        actual_result = Integer(dummy).not_in([10], "columm")
        excepted_result = {
            "score": 1.0,
            "valid": 25,
            "invalid": 0,
            "warning": {},
        }

        self.assertDictEqual(actual_result, excepted_result, MESSAGE)

    def test_not_in_invalid(self):
        """test_not_in_invalid."""
        dummy = pd.concat(
            [
                pd.DataFrame({"columm": np.random.randint(0, 10, 25)}),
                pd.DataFrame(
                    [{"columm": -5}, {"columm": 10}, {"columm": "10"}]
                ),
            ]
        )

        actual_result = Integer(dummy).not_in([10], "columm")
        excepted_result = {
            "score": 0.9285714285714286,
            "valid": 26,
            "invalid": 2,
            "warning": {
                26: create_warning_data(10, "Value should be not in [10]"),
                27: create_warning_data(
                    "10",
                    WarningDataDetailMessage.INTEGER_DATA_TYPE,
                    WarningDataMessage.INVALID_DATA_TYPE,
                ),
            },
        }

        self.assertDictEqual(actual_result, excepted_result, MESSAGE)

    def test_length_valid(self):
        """test_length_valid."""
        dummy = pd.DataFrame({"columm": np.random.randint(0, 10, 25)})

        actual_result = Integer(dummy).length(1, "columm")
        excepted_result = {
            "score": 1.0,
            "valid": 25,
            "invalid": 0,
            "warning": {},
        }

        self.assertDictEqual(actual_result, excepted_result, MESSAGE)

    def test_length_invalid(self):
        """test_length_invalid."""
        dummy = pd.concat(
            [
                pd.DataFrame({"columm": np.random.randint(0, 10, 25)}),
                pd.DataFrame(
                    [{"columm": -5}, {"columm": 10}, {"columm": "10"}]
                ),
            ]
        )

        actual_result = Integer(dummy).length(1, "columm")
        excepted_result = {
            "score": 0.8928571428571429,
            "valid": 25,
            "invalid": 3,
            "warning": {
                25: create_warning_data(-5, "Value should have a length of 1"),
                26: create_warning_data(10, "Value should have a length of 1"),
                27: create_warning_data(
                    "10",
                    WarningDataDetailMessage.INTEGER_DATA_TYPE,
                    WarningDataMessage.INVALID_DATA_TYPE,
                ),
            },
        }

        self.assertDictEqual(actual_result, excepted_result, MESSAGE)

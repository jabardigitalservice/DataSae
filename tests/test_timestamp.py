#!/usr/bin/env python3

# Copyright (C) Free Software Foundation, Inc. All rights reserved.
# Licensed under the AGPL-3.0-only License. See LICENSE in the project root
# for license information.

"""test_timestamp."""

from datetime import datetime, timedelta
import unittest

import pandas as pd

from datasae.timestamp import Timestamp, WarningDataDetailMessage
from datasae.utils import create_warning_data, WarningDataMessage
from . import MESSAGE


class TimestampTest(unittest.TestCase):
    """TimestampTest."""

    def __init__(self, methodName: str = "TimestampTest"):
        """__init__."""
        super().__init__(methodName)
        self.maxDiff = None

    def test_equal_to_valid(self):
        """test_equal_to_valid."""
        timestamp = datetime.now()

        dummy = pd.DataFrame({"columm": [timestamp for i in range(25)]})

        actual_result = Timestamp(dummy).equal_to(timestamp, "columm")
        excepted_result = {
            "score": 1.0,
            "valid": 25,
            "invalid": 0,
            "warning": {},
        }

        self.assertDictEqual(actual_result, excepted_result, MESSAGE)

    def test_equal_to_invalid(self):
        """test_equal_to_invalid."""
        timestamp = datetime.now()
        timestamp_invalid = datetime.now()

        dummy = pd.concat(
            [
                pd.DataFrame({"columm": [timestamp for i in range(25)]}),
                pd.DataFrame(
                    [
                        {"columm": None},
                        {"columm": "2023-09-26 14:32:46.527593"},
                        {"columm": timestamp_invalid},
                    ]
                ),
            ]
        ).reset_index(drop=True)

        actual_result = Timestamp(dummy).equal_to(timestamp, "columm")
        excepted_result = {
            "score": 0.8928571428571429,
            "valid": 25,
            "invalid": 3,
            "warning": {
                25: create_warning_data(
                    None,
                    WarningDataDetailMessage.timestamp_data_type,
                    WarningDataMessage.INVALID_DATA_TYPE,
                ),
                26: create_warning_data(
                    "2023-09-26 14:32:46.527593",
                    WarningDataDetailMessage.timestamp_data_type,
                    WarningDataMessage.INVALID_DATA_TYPE,
                ),
                27: create_warning_data(
                    timestamp_invalid, f"Value should be equal to {timestamp}"
                ),
            },
        }

        self.assertDictEqual(actual_result, excepted_result, MESSAGE)

    def test_less_than_valid(self):
        """test_less_than_valid."""
        timestamp = datetime.now()

        dummy = pd.DataFrame({"columm": [timestamp for i in range(25)]})

        actual_result = Timestamp(dummy).less_than(datetime.now(), "columm")
        excepted_result = {
            "score": 1.0,
            "valid": 25,
            "invalid": 0,
            "warning": {},
        }

        self.assertDictEqual(actual_result, excepted_result, MESSAGE)

    def test_less_than_invalid(self):
        """test_less_than_invalid."""
        timestamp = datetime.now()
        timestamp_invalid = datetime.now() + timedelta(days=1)
        timestamp_condition = datetime.now()

        dummy = pd.concat(
            [
                pd.DataFrame({"columm": [timestamp for i in range(25)]}),
                pd.DataFrame(
                    [
                        {"columm": None},
                        {"columm": "2023-09-26 14:32:46.527593"},
                        {"columm": timestamp_invalid},
                    ]
                ),
            ]
        ).reset_index(drop=True)

        actual_result = Timestamp(dummy).less_than(
            timestamp_condition, "columm"
        )
        excepted_result = {
            "score": 0.8928571428571429,
            "valid": 25,
            "invalid": 3,
            "warning": {
                25: create_warning_data(
                    None,
                    WarningDataDetailMessage.timestamp_data_type,
                    WarningDataMessage.INVALID_DATA_TYPE,
                ),
                26: create_warning_data(
                    "2023-09-26 14:32:46.527593",
                    WarningDataDetailMessage.timestamp_data_type,
                    WarningDataMessage.INVALID_DATA_TYPE,
                ),
                27: create_warning_data(
                    timestamp_invalid,
                    f"Value should be less than {timestamp_condition}",
                ),
            },
        }

        self.assertDictEqual(actual_result, excepted_result, MESSAGE)

    def test_less_than_equal_valid(self):
        """test_less_than_equal_valid."""
        timestamp = datetime.now()

        dummy = pd.DataFrame({"columm": [timestamp for i in range(25)]})

        actual_result = Timestamp(dummy).less_than_equal(
            timestamp + timedelta(hours=1), "columm"
        )
        excepted_result = {
            "score": 1.0,
            "valid": 25,
            "invalid": 0,
            "warning": {},
        }

        self.assertDictEqual(actual_result, excepted_result, MESSAGE)

    def test_less_than_equal_invalid(self):
        """test_less_than_equal_invalid."""
        timestamp = datetime.now()
        timestamp_invalid = datetime.now() + timedelta(days=1)
        timestamp_condition = datetime.now()

        dummy = pd.concat(
            [
                pd.DataFrame({"columm": [timestamp for i in range(25)]}),
                pd.DataFrame(
                    [
                        {"columm": None},
                        {"columm": "2023-09-26 14:32:46.527593"},
                        {"columm": timestamp_invalid},
                    ]
                ),
            ]
        ).reset_index(drop=True)

        actual_result = Timestamp(dummy).less_than_equal(
            timestamp_condition, "columm"
        )
        excepted_result = {
            "score": 0.8928571428571429,
            "valid": 25,
            "invalid": 3,
            "warning": {
                25: create_warning_data(
                    None,
                    WarningDataDetailMessage.timestamp_data_type,
                    WarningDataMessage.INVALID_DATA_TYPE,
                ),
                26: create_warning_data(
                    "2023-09-26 14:32:46.527593",
                    WarningDataDetailMessage.timestamp_data_type,
                    WarningDataMessage.INVALID_DATA_TYPE,
                ),
                27: create_warning_data(
                    timestamp_invalid,
                    f"Value should be less than equal {timestamp_condition}",
                ),
            },
        }

        self.assertDictEqual(actual_result, excepted_result, MESSAGE)

    def test_greater_than_valid(self):
        """test_greater_than_valid."""
        timestamp = datetime.now()

        dummy = pd.DataFrame({"columm": [timestamp for i in range(25)]})

        actual_result = Timestamp(dummy).greater_than(
            (timestamp - timedelta(hours=1)), "columm"
        )
        excepted_result = {
            "score": 1.0,
            "valid": 25,
            "invalid": 0,
            "warning": {},
        }

        self.assertDictEqual(actual_result, excepted_result, MESSAGE)

    def test_greater_than_invalid(self):
        """test_greater_than_invalid."""
        timestamp = datetime.now()
        timestamp_invalid = datetime.now() - timedelta(days=2)
        timestamp_condition = datetime.now() - timedelta(days=1)

        dummy = pd.concat(
            [
                pd.DataFrame({"columm": [timestamp for i in range(25)]}),
                pd.DataFrame(
                    [
                        {"columm": None},
                        {"columm": "2022-09-26 14:32:46.527593"},
                        {"columm": timestamp_invalid},
                    ]
                ),
            ]
        ).reset_index(drop=True)

        actual_result = Timestamp(dummy).greater_than(
            timestamp_condition, "columm"
        )
        excepted_result = {
            "score": 0.8928571428571429,
            "valid": 25,
            "invalid": 3,
            "warning": {
                25: create_warning_data(
                    None,
                    WarningDataDetailMessage.timestamp_data_type,
                    WarningDataMessage.INVALID_DATA_TYPE,
                ),
                26: create_warning_data(
                    "2022-09-26 14:32:46.527593",
                    WarningDataDetailMessage.timestamp_data_type,
                    WarningDataMessage.INVALID_DATA_TYPE,
                ),
                27: create_warning_data(
                    timestamp_invalid,
                    f"Value should be greater than {timestamp_condition}",
                ),
            },
        }

        self.assertDictEqual(actual_result, excepted_result, MESSAGE)

    def test_greater_than_equal_valid(self):
        """test_greater_than_equal_valid."""
        timestamp = datetime.now()

        dummy = pd.DataFrame({"columm": [timestamp for i in range(25)]})

        actual_result = Timestamp(dummy).greater_than_equal(
            timestamp, "columm"
        )
        excepted_result = {
            "score": 1.0,
            "valid": 25,
            "invalid": 0,
            "warning": {},
        }

        self.assertDictEqual(actual_result, excepted_result, MESSAGE)

    def test_greater_than_equal_invalid(self):
        """test_greater_than_equal_invalid."""
        timestamp = datetime.now()
        timestamp_invalid = datetime.now() - timedelta(days=1)

        dummy = pd.concat(
            [
                pd.DataFrame({"columm": [timestamp for i in range(25)]}),
                pd.DataFrame(
                    [
                        {"columm": None},
                        {"columm": "2023-09-26 14:32:46.527593"},
                        {"columm": timestamp_invalid},
                    ]
                ),
            ]
        ).reset_index(drop=True)

        actual_result = Timestamp(dummy).greater_than_equal(
            timestamp, "columm"
        )
        excepted_result = {
            "score": 0.8928571428571429,
            "valid": 25,
            "invalid": 3,
            "warning": {
                25: create_warning_data(
                    None,
                    WarningDataDetailMessage.timestamp_data_type,
                    WarningDataMessage.INVALID_DATA_TYPE,
                ),
                26: create_warning_data(
                    "2023-09-26 14:32:46.527593",
                    WarningDataDetailMessage.timestamp_data_type,
                    WarningDataMessage.INVALID_DATA_TYPE,
                ),
                27: create_warning_data(
                    timestamp_invalid,
                    f"Value should be greater than equal {timestamp}",
                ),
            },
        }

        self.assertDictEqual(actual_result, excepted_result, MESSAGE)

    def test_in_range_valid(self):
        """test_in_range_valid."""
        timestamp = datetime.now()

        dummy = pd.DataFrame({"columm": [timestamp for i in range(25)]})

        actual_result = Timestamp(dummy).in_range(
            timestamp - timedelta(hours=1),
            timestamp + timedelta(hours=1),
            "columm",
        )
        excepted_result = {
            "score": 1.0,
            "valid": 25,
            "invalid": 0,
            "warning": {},
        }

        self.assertDictEqual(actual_result, excepted_result, MESSAGE)

    def test_in_range_invalid(self):
        """test_in_range_invalid."""
        timestamp = datetime.now()

        timestamp = datetime.now()
        timestamp_invalid = datetime.now() - timedelta(days=1)

        dummy = pd.concat(
            [
                pd.DataFrame({"columm": [timestamp for i in range(25)]}),
                pd.DataFrame(
                    [
                        {"columm": None},
                        {"columm": "2023-09-26 14:32:46.527593"},
                        {"columm": timestamp_invalid},
                    ]
                ),
            ]
        ).reset_index(drop=True)

        actual_result = Timestamp(dummy).in_range(
            timestamp - timedelta(hours=1),
            timestamp + timedelta(hours=1),
            "columm",
        )
        excepted_result = {
            "score": 0.8928571428571429,
            "valid": 25,
            "invalid": 3,
            "warning": {
                25: create_warning_data(
                    None,
                    WarningDataDetailMessage.timestamp_data_type,
                    WarningDataMessage.INVALID_DATA_TYPE,
                ),
                26: create_warning_data(
                    "2023-09-26 14:32:46.527593",
                    WarningDataDetailMessage.timestamp_data_type,
                    WarningDataMessage.INVALID_DATA_TYPE,
                ),
                27: create_warning_data(
                    timestamp_invalid,
                    (
                        "Value should be in the range of "
                        f"{timestamp - timedelta(hours=1)} "
                        f"and {timestamp + timedelta(hours=1)}"
                    ),
                ),
            },
        }

        self.assertDictEqual(actual_result, excepted_result, MESSAGE)

    def test_is_in_valid(self):
        """test_is_in_valid."""
        timestamp = datetime.now()

        dummy = pd.DataFrame({"columm": [timestamp for i in range(25)]})

        actual_result = Timestamp(dummy).is_in([timestamp], "columm")
        excepted_result = {
            "score": 1.0,
            "valid": 25,
            "invalid": 0,
            "warning": {},
        }

        self.assertDictEqual(actual_result, excepted_result, MESSAGE)

    def test_is_in_invalid(self):
        """test_is_in_invalid."""
        timestamp = datetime.now()

        timestamp_invalid = datetime.now() - timedelta(days=1)

        dummy = pd.concat(
            [
                pd.DataFrame({"columm": [timestamp for i in range(25)]}),
                pd.DataFrame(
                    [
                        {"columm": None},
                        {"columm": "2023-09-26 14:32:46.527593"},
                        {"columm": timestamp_invalid},
                    ]
                ),
            ]
        ).reset_index(drop=True)

        actual_result = Timestamp(dummy).is_in([timestamp], "columm")
        excepted_result = {
            "score": 0.8928571428571429,
            "valid": 25,
            "invalid": 3,
            "warning": {
                25: create_warning_data(
                    None,
                    WarningDataDetailMessage.timestamp_data_type,
                    WarningDataMessage.INVALID_DATA_TYPE,
                ),
                26: create_warning_data(
                    "2023-09-26 14:32:46.527593",
                    WarningDataDetailMessage.timestamp_data_type,
                    WarningDataMessage.INVALID_DATA_TYPE,
                ),
                27: create_warning_data(
                    timestamp_invalid,
                    (f"Value should be in {[timestamp]}"),
                ),
            },
        }

        self.assertDictEqual(actual_result, excepted_result, MESSAGE)

    def test_not_in_valid(self):
        """test_not_in_valid."""
        timestamp = datetime.now()

        dummy = pd.DataFrame({"columm": [timestamp for i in range(25)]})

        actual_result = Timestamp(dummy).not_in(
            [timestamp + timedelta(hours=1)], "columm"
        )
        excepted_result = {
            "score": 1.0,
            "valid": 25,
            "invalid": 0,
            "warning": {},
        }

        self.assertDictEqual(actual_result, excepted_result, MESSAGE)

    def test_not_in_invalid(self):
        """test_not_in_invalid."""
        timestamp = datetime.now()

        timestamp_invalid = datetime.now() - timedelta(days=1)

        dummy = pd.concat(
            [
                pd.DataFrame({"columm": [timestamp for i in range(25)]}),
                pd.DataFrame(
                    [
                        {"columm": None},
                        {"columm": "2023-09-26 14:32:46.527593"},
                        {"columm": timestamp_invalid},
                    ]
                ),
            ]
        ).reset_index(drop=True)

        actual_result = Timestamp(dummy).not_in([timestamp_invalid], "columm")
        excepted_result = {
            "score": 0.8928571428571429,
            "valid": 25,
            "invalid": 3,
            "warning": {
                25: create_warning_data(
                    None,
                    WarningDataDetailMessage.timestamp_data_type,
                    WarningDataMessage.INVALID_DATA_TYPE,
                ),
                26: create_warning_data(
                    "2023-09-26 14:32:46.527593",
                    WarningDataDetailMessage.timestamp_data_type,
                    WarningDataMessage.INVALID_DATA_TYPE,
                ),
                27: create_warning_data(
                    timestamp_invalid,
                    (f"Value should be not in {[timestamp_invalid]}"),
                ),
            },
        }

        self.assertDictEqual(actual_result, excepted_result, MESSAGE)

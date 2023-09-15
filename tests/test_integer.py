#!/usr/bin/env python3

# This module is part of DataSae and is released under
# the AGPL-3.0-only License: https://opensource.org/license/agpl-v3/

import unittest

import numpy as np
import pandas as pd

from datasae.integer import Integer, WarningDataDetailMessage
from datasae.utils import create_warning_data, WarningDataMessage


MESSAGE: str = 'Result Not Match'


class IntegerTest(unittest.TestCase):
    def __init__(self, methodName: str = 'TestInteger'):
        super().__init__(methodName)
        self.maxDiff = None

    def test_less_valid(self):
        dummy = pd.DataFrame({'columm': np.random.randint(0, 10, 25)})

        actual_result = Integer(dummy).less_than(10, 'columm')
        excepted_result = {
            'score': 1.0,
            'valid': 25,
            'invalid': 0,
            'warning': {}
        }

        self.assertDictEqual(actual_result, excepted_result, MESSAGE)

    def test_less_invalid(self):
        dummy = pd.concat([
            pd.DataFrame({'columm': np.random.randint(0, 10, 20)}),
            pd.DataFrame([
                {'columm': '11'},
                {'columm': 44},
                {'columm': 10.2},
                {'columm': -1}
            ])
        ])

        actual_result = Integer(dummy).less_than(10, 'columm')
        excepted_result = {
            'score': 0.875,
            'valid': 21,
            'invalid': 3,
            'warning': {
                20: create_warning_data(
                    '11',
                    WarningDataDetailMessage.INTEGER_DATA_TYPE,
                    WarningDataMessage.INVALID_DATA_TYPE
                ),
                21: create_warning_data(
                    44,
                    'Value should be less than 10'
                ),
                22: create_warning_data(
                    10.2,
                    WarningDataDetailMessage.INTEGER_DATA_TYPE,
                    WarningDataMessage.INVALID_DATA_TYPE
                )
            }
        }

        self.assertDictEqual(actual_result, excepted_result, MESSAGE)

    def test_in_range_valid(self):
        dummy = pd.DataFrame({'columm': np.random.randint(0, 10, 25)})

        actual_result = Integer(dummy).in_range(-2, 11, 'columm')
        excepted_result = {
            'score': 1.,
            'valid': 25,
            'invalid': 0,
            'warning': {}
        }

        self.assertDictEqual(actual_result, excepted_result, MESSAGE)

    def test_in_range_invalid(self):
        dummy = pd.concat([
            pd.DataFrame({'columm': np.random.randint(0, 10, 25)}),
            pd.DataFrame([
                {'columm': -5},
                {'columm': 44}
            ])
        ])

        actual_result = Integer(dummy).in_range(-2, 11, 'columm')
        excepted_result = {
            'score': .9259259259259259,
            'valid': 25,
            'invalid': 2,
            'warning': {
                25: create_warning_data(
                    -5, 'Value should be in the range of -2 and 11'
                ),
                26: create_warning_data(
                    44, 'Value should be in the range of -2 and 11'
                )
            }
        }

        self.assertDictEqual(actual_result, excepted_result, MESSAGE)

    def test_is_in_valid(self):
        dummy = pd.DataFrame({'columm': np.random.randint(0, 10, 25)})

        actual_result = Integer(dummy).is_in(range(10), 'columm')
        excepted_result = {
            'score': 1.,
            'valid': 25,
            'invalid': 0,
            'warning': {}
        }

        self.assertDictEqual(actual_result, excepted_result, MESSAGE)

    def test_is_in_invalid(self):
        dummy = pd.concat([
            pd.DataFrame({'columm': np.random.randint(0, 10, 25)}),
            pd.DataFrame([
                {'columm': -5},
                {'columm': 44}
            ])
        ])

        actual_result = Integer(dummy).is_in(range(10), 'columm')
        excepted_result = {
            'score': .9259259259259259,
            'valid': 25,
            'invalid': 2,
            'warning': {
                25: create_warning_data(
                    -5, 'Value should be in range(0, 10)'
                ),
                26: create_warning_data(
                    44, 'Value should be in range(0, 10)'
                )
            }
        }

        self.assertDictEqual(actual_result, excepted_result, MESSAGE)

    def test_not_in_valid(self):
        dummy = pd.DataFrame({'columm': np.random.randint(0, 10, 25)})

        actual_result = Integer(dummy).not_in([10], 'columm')
        excepted_result = {
            'score': 1.,
            'valid': 25,
            'invalid': 0,
            'warning': {}
        }

        self.assertDictEqual(actual_result, excepted_result, MESSAGE)

    def test_not_in_invalid(self):
        dummy = pd.concat([
            pd.DataFrame({'columm': np.random.randint(0, 10, 25)}),
            pd.DataFrame([
                {'columm': -5},
                {'columm': 10}
            ])
        ])

        actual_result = Integer(dummy).not_in([10], 'columm')
        excepted_result = {
            'score': .9629629629629629,
            'valid': 26,
            'invalid': 1,
            'warning': {
                26: create_warning_data(
                    10, 'Value should be not in [10]'
                )
            }
        }

        self.assertDictEqual(actual_result, excepted_result, MESSAGE)

    def test_length_valid(self):
        dummy = pd.DataFrame({'columm': np.random.randint(0, 10, 25)})

        actual_result = Integer(dummy).length(1, 'columm')
        excepted_result = {
            'score': 1.,
            'valid': 25,
            'invalid': 0,
            'warning': {}
        }

        self.assertDictEqual(actual_result, excepted_result, MESSAGE)

    def test_length_invalid(self):
        dummy = pd.concat([
            pd.DataFrame({'columm': np.random.randint(0, 10, 25)}),
            pd.DataFrame([
                {'columm': -5},
                {'columm': 10}
            ])
        ])

        actual_result = Integer(dummy).length(1, 'columm')
        excepted_result = {
            'score': .9259259259259259,
            'valid': 25,
            'invalid': 2,
            'warning': {
                25: create_warning_data(
                    -5, 'Value should have a length of 1'
                ),
                26: create_warning_data(
                    10, 'Value should have a length of 1'
                )
            }
        }

        self.assertDictEqual(actual_result, excepted_result, MESSAGE)


if __name__ == '__main__':
    unittest.main()

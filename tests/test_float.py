#!/usr/bin/env python3

# Copyright (C) Free Software Foundation, Inc. All rights reserved.
# Licensed under the AGPL-3.0-only License. See LICENSE in the project root
# for license information.

"""test_float."""

import unittest

import numpy as np
import pandas as pd

from datasae.float import Float, WarningDataDetailMessage
from datasae.utils import create_warning_data, WarningDataMessage

from . import MESSAGE


class FloatTest(unittest.TestCase):
    """FloatTest."""

    def __init__(self, methodName: str = 'TestFloat'):
        """__init__."""
        super().__init__(methodName)
        self.maxDiff = None
        self.dummy = pd.DataFrame({'columm': np.random.uniform(.0, 1., 20)})

    def test_equal_to(self):
        """test_equal_to."""
        dummy = pd.DataFrame([
            {'columm': -.5}, {'columm': .0}, {'columm': '1.0'}
        ])

        actual_result = Float(dummy).equal_to(-.5, 'columm')
        excepted_result = {
            'score': .3333333333333333,
            'valid': 1,
            'invalid': 2,
            'warning': {
                1: create_warning_data(
                    .0, 'Value should be equal to -0.5'
                ),
                2: create_warning_data(
                    '1.0',
                    WarningDataDetailMessage.FLOAT_DATA_TYPE,
                    WarningDataMessage.INVALID_DATA_TYPE
                )
            }
        }

        self.assertDictEqual(actual_result, excepted_result, MESSAGE)

    def test_less_valid(self):
        """test_less_valid."""
        dummy = self.dummy

        actual_result = Float(dummy).less_than(1., 'columm')
        excepted_result = {
            'score': 1.,
            'valid': 20,
            'invalid': 0,
            'warning': {}
        }

        self.assertDictEqual(actual_result, excepted_result, MESSAGE)

    def test_less_invalid(self):
        """test_less_invalid."""
        dummy = pd.concat([
            self.dummy,
            pd.DataFrame([
                {'columm': '0.5'},
                {'columm': -.5},
                {'columm': 1.}
            ])
        ])

        actual_result = Float(dummy).less_than(1., 'columm')
        excepted_result = {
            'score': .9130434782608695,
            'valid': 21,
            'invalid': 2,
            'warning': {
                20: create_warning_data(
                    '0.5',
                    WarningDataDetailMessage.FLOAT_DATA_TYPE,
                    WarningDataMessage.INVALID_DATA_TYPE
                ),
                22: create_warning_data(
                    1.,
                    'Value should be less than 1.0'
                )
            }
        }

        self.assertDictEqual(actual_result, excepted_result, MESSAGE)

    def test_less_equal_valid(self):
        """test_less_equal_valid."""
        dummy = self.dummy

        actual_result = Float(dummy).less_than_equal(1., 'columm')
        excepted_result = {
            'score': 1.,
            'valid': 20,
            'invalid': 0,
            'warning': {}
        }

        self.assertDictEqual(actual_result, excepted_result, MESSAGE)

    def test_less_equal_invalid(self):
        """test_less_equal_invalid."""
        dummy = pd.concat([
            self.dummy,
            pd.DataFrame([
                {'columm': '0.5'},
                {'columm': -.5},
                {'columm': 1.},
                {'columm': 1.5}
            ])
        ])

        actual_result = Float(dummy).less_than_equal(1., 'columm')
        excepted_result = {
            'score': .9166666666666666,
            'valid': 22,
            'invalid': 2,
            'warning': {
                20: create_warning_data(
                    '0.5',
                    WarningDataDetailMessage.FLOAT_DATA_TYPE,
                    WarningDataMessage.INVALID_DATA_TYPE
                ),
                23: create_warning_data(
                    1.5,
                    'Value should be less than equal 1.0'
                )
            }
        }

        self.assertDictEqual(actual_result, excepted_result, MESSAGE)

    def test_greater_valid(self):
        """test_greater_valid."""
        dummy = self.dummy

        actual_result = Float(dummy).greater_than(.0, 'columm')
        excepted_result = {
            'score': 1.,
            'valid': 20,
            'invalid': 0,
            'warning': {}
        }

        self.assertDictEqual(actual_result, excepted_result, MESSAGE)

    def test_greater_invalid(self):
        """test_greater_invalid."""
        dummy = pd.concat([
            self.dummy,
            pd.DataFrame([
                {'columm': '0.5'},
                {'columm': -.5},
                {'columm': .0}
            ])
        ])

        actual_result = Float(dummy).greater_than(.0, 'columm')
        excepted_result = {
            'score': .8695652173913043,
            'valid': 20,
            'invalid': 3,
            'warning': {
                20: create_warning_data(
                    '0.5',
                    WarningDataDetailMessage.FLOAT_DATA_TYPE,
                    WarningDataMessage.INVALID_DATA_TYPE
                ),
                21: create_warning_data(
                    -.5,
                    'Value should be greater than 0.0'
                ),
                22: create_warning_data(
                    .0,
                    'Value should be greater than 0.0'
                )
            }
        }

        self.assertDictEqual(actual_result, excepted_result, MESSAGE)

    def test_greater_equal_valid(self):
        """test_greater_equal_valid."""
        dummy = self.dummy

        actual_result = Float(dummy).greater_than_equal(.0, 'columm')
        excepted_result = {
            'score': 1.,
            'valid': 20,
            'invalid': 0,
            'warning': {}
        }

        self.assertDictEqual(actual_result, excepted_result, MESSAGE)

    def test_greater_equal_invalid(self):
        """test_greater_equal_invalid."""
        dummy = pd.concat([
            self.dummy,
            pd.DataFrame([
                {'columm': '0.5'},
                {'columm': -.5},
                {'columm': .0}
            ])
        ])

        actual_result = Float(dummy).greater_than_equal(.0, 'columm')
        excepted_result = {
            'score': .9130434782608695,
            'valid': 21,
            'invalid': 2,
            'warning': {
                20: create_warning_data(
                    '0.5',
                    WarningDataDetailMessage.FLOAT_DATA_TYPE,
                    WarningDataMessage.INVALID_DATA_TYPE
                ),
                21: create_warning_data(
                    -.5,
                    'Value should be greater than equal 0.0'
                )
            }
        }

        self.assertDictEqual(actual_result, excepted_result, MESSAGE)

    def test_in_range(self):
        """test_in_range."""
        dummy = pd.concat([
            self.dummy,
            pd.DataFrame([{'columm': '0.5'}, {'columm': 1.1}])
        ])

        actual_result = Float(dummy).in_range(.0, 1., 'columm')
        excepted_result = {
            'score': .9090909090909091,
            'valid': 20,
            'invalid': 2,
            'warning': {
                20: create_warning_data(
                    '0.5',
                    WarningDataDetailMessage.FLOAT_DATA_TYPE,
                    WarningDataMessage.INVALID_DATA_TYPE
                ),
                21: create_warning_data(
                    1.1,
                    'Value should be in the range of 0.0 and 1.0'
                )
            }
        }

        self.assertDictEqual(actual_result, excepted_result, MESSAGE)

    def test_is_in(self):
        """test_is_in."""
        dummy = pd.DataFrame([
            {'columm': 1.}, {'columm': .0}, {'columm': '0.5'}
        ])

        actual_result = Float(dummy).is_in([1.], 'columm')
        excepted_result = {
            'score': .3333333333333333,
            'valid': 1,
            'invalid': 2,
            'warning': {
                1: create_warning_data(.0, 'Value should be in [1.0]'),
                2: create_warning_data(
                    '0.5',
                    WarningDataDetailMessage.FLOAT_DATA_TYPE,
                    WarningDataMessage.INVALID_DATA_TYPE
                )
            }
        }

        self.assertDictEqual(actual_result, excepted_result, MESSAGE)

    def test_not_in(self):
        """test_not_in."""
        dummy = pd.DataFrame([
            {'columm': 1.}, {'columm': .0}, {'columm': '0.5'}
        ])

        actual_result = Float(dummy).not_in([1.], 'columm')
        excepted_result = {
            'score': .3333333333333333,
            'valid': 1,
            'invalid': 2,
            'warning': {
                0: create_warning_data(1., 'Value should be not in [1.0]'),
                2: create_warning_data(
                    '0.5',
                    WarningDataDetailMessage.FLOAT_DATA_TYPE,
                    WarningDataMessage.INVALID_DATA_TYPE
                )
            }
        }

        self.assertDictEqual(actual_result, excepted_result, MESSAGE)

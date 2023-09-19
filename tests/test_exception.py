#!/usr/bin/env python3

# This module is part of DataSae and is released under
# the AGPL-3.0-only License: https://opensource.org/license/agpl-v3/

import unittest

from datasae.exception import (
    EmptyDataFrame,
    ColumnNotExist,
    InvalidDateFormatWarning
)


class ExceptionTest(unittest.TestCase):
    def test_exception(self):
        self.assertEqual(EmptyDataFrame().message, 'DataFrame is empty.')
        self.assertEqual(
            ColumnNotExist('column').message,
            "Column 'column' does not exist in the DataFrame."
        )
        self.assertEqual(
            InvalidDateFormatWarning('warning').message,
            'warning'
        )

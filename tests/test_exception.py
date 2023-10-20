#!/usr/bin/env python3

# Copyright (c) Free Software Foundation, Inc. All rights reserved.
# Licensed under the AGPL-3.0-only License. See LICENSE in the project root
# for license information.

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

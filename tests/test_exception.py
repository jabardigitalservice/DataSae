#!/usr/bin/env python3

# Copyright (C) Free Software Foundation, Inc. All rights reserved.
# Licensed under the AGPL-3.0-only License. See LICENSE in the project root
# for license information.

"""test_exception."""

import unittest

from datasae.exception import (
    EmptyDataFrame,
    ColumnNotExist,
    InvalidDateFormatWarning
)


class ExceptionTest(unittest.TestCase):
    """ExceptionTest."""

    def test_exception(self):
        """test_exception."""
        self.assertEqual(EmptyDataFrame().message, 'DataFrame is empty.')
        self.assertEqual(
            ColumnNotExist('column').message,
            "Column 'column' does not exist in the DataFrame."
        )
        self.assertEqual(
            InvalidDateFormatWarning('warning').message,
            'warning'
        )

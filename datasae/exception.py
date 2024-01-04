#!/usr/bin/env python3

# Copyright (C) Free Software Foundation, Inc. All rights reserved.
# Licensed under the AGPL-3.0-only License. See LICENSE in the project root
# for license information.

"""Exception library."""


class EmptyDataFrame(Exception):
    """Exception class that is raised when a DataFrame object is empty."""

    def __init__(self):
        """__init__ method."""
        message = 'DataFrame is empty.'
        super().__init__(message)
        self.message = message


class ColumnNotExist(Exception):
    """Exception class that is raised when a column not exist."""

    def __init__(self, column):
        """__init__ method."""
        message = f"Column '{column}' does not exist in the DataFrame."
        super().__init__(message)
        self.message = message


class InvalidDataTypeWarning(Exception):
    """Exception class that is raised when a invalid data type."""

    def __init__(self, warning_data):
        """__init__ method."""
        self.warning_data = warning_data
        message = warning_data
        super().__init__(message)
        self.message = message


class InvalidDateFormatWarning(Exception):
    """Exception class that is raised when a invalid date format."""

    def __init__(self, warning_data):
        """__init__ method."""
        self.warning_data = warning_data
        message = warning_data
        super().__init__(message)
        self.message = message


class InvalidDataValueWarning(Exception):
    """Exception class that is raised when a invalid data format."""

    def __init__(self, warning_data):
        """__init__ method."""
        self.warning_data = warning_data
        message = warning_data
        super().__init__(message)
        self.message = message

#!/usr/bin/env python3

# This module is part of DataSae and is released under
# the AGPL-3.0-only License: https://opensource.org/license/agpl-v3/


class EmptyDataFrame(Exception):
    def __init__(self):
        message = 'DataFrame is empty.'
        super().__init__(message)
        self.message = message


class ColumnNotExist(Exception):
    def __init__(self, column):
        message = f"Column '{column}' does not exist in the DataFrame."
        super().__init__(message)
        self.message = message


class InvalidDataTypeWarning(Exception):
    def __init__(self, warning_data):
        self.warning_data = warning_data
        message = warning_data
        super().__init__(message)
        self.message = message


class InvalidDateFormatWarning(Exception):
    def __init__(self, warning_data):
        self.warning_data = warning_data
        message = warning_data
        super().__init__(message)
        self.message = message


class InvalidDataValueWarning(Exception):
    def __init__(self, warning_data):
        self.warning_data = warning_data
        message = warning_data
        super().__init__(message)
        self.message = message

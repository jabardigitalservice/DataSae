#!/usr/bin/env python3

# Copyright (c) Free Software Foundation, Inc. All rights reserved.
# Licensed under the AGPL-3.0-only License. See LICENSE in the project root
# for license information.


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

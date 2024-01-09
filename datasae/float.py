#!/usr/bin/env python3

# Copyright (C) Free Software Foundation, Inc. All rights reserved.
# Licensed under the AGPL-3.0-only License. See LICENSE in the project root
# for license information.

"""Float library."""

import pandas as pd

from .exception import InvalidDataTypeWarning, InvalidDataValueWarning
from .utils import Basic, create_warning_data, WarningDataMessage


class WarningDataDetailMessage:
    """Provides warning messages for different data types."""

    FLOAT_DATA_TYPE: str = "Value must be of float data type"


class Float(Basic):
    """Float class."""

    def __init__(self, dataFrame: pd.DataFrame):
        """
        __init__ method.

        Initializes an instance of the Float class.

        Args:
            dataFrame (pd.DataFrame): The data you want to process.
        """
        self.dataFrame = dataFrame

    @staticmethod
    def check_equal(float_data: float, value: float) -> tuple:
        """
        Check if a given float value is equal to a specified value.

        Args:
            float_data (float): The float value to be checked.
            value (float): The specified value to compare against.

        Returns:
            tuple: A tuple containing the following elements:
                - valid (float): The number of valid values (either 0 or 1).
                - invalid(float): The number of invalid values (either 0 or 1).
                - warning_data (dict): A dictionary with warning data if the
                    value is invalid, including the warning message,
                    the actual value, and a detailed message.
        """
        valid = 0
        invalid = 0
        warning_data = {}

        if float_data == value:
            valid = 1
        else:
            invalid = 1
            warning_data = create_warning_data(
                float_data,
                f"Value should be equal to {value}"
            )

        return valid, invalid, warning_data

    @staticmethod
    def check_less_than(float_data: float, value: float) -> tuple:
        """
        Check if a given float value is less than to a specified value.

        Args:
            float_data (float): The float value to be checked.
            value (float): The specified value to compare against.

        Returns:
            tuple: A tuple containing the following elements:
                - valid (float): The number of valid values (either 0 or 1).
                - invalid(float): The number of invalid values (either 0 or 1).
                - warning_data (dict): A dictionary with warning data if the
                    value is invalid, including the warning message,
                    the actual value, and a detailed message.
        """
        valid = 0
        invalid = 0
        warning_data = {}

        if float_data < value:
            valid = 1
        else:
            invalid = 1
            warning_data = create_warning_data(
                float_data, f"Value should be less than {value}"
            )

        return valid, invalid, warning_data

    @staticmethod
    def check_less_than_equal(float_data: float, value: float) -> tuple:
        """
        check_less_than_equal method.

        Check if a given float value is less than
            or equal to a specified value.

        Args:
            float_data (float): The float value to be checked.
            value (float): The specified value to compare against.

        Returns:
            tuple: A tuple containing the following elements:
                - valid (float): The number of valid values (either 0 or 1).
                - invalid(float): The number of invalid values (either 0 or 1).
                - warning_data (dict): A dictionary with warning data if the
                    value is invalid, including the warning message,
                    the actual value, and a detailed message.
        """
        valid = 0
        invalid = 0
        warning_data = {}

        if float_data <= value:
            valid = 1
        else:
            invalid = 1
            warning_data = create_warning_data(
                float_data, f"Value should be less than equal {value}"
            )

        return valid, invalid, warning_data

    @staticmethod
    def check_greater_than(float_data: float, value: float) -> tuple:
        """
        Check if a given float value is greater than to a specified value.

        Args:
            float_data (float): The float value to be checked.
            value (float): The specified value to compare against.

        Returns:
            tuple: A tuple containing the following elements:
                - valid (float): The number of valid values (either 0 or 1).
                - invalid(float): The number of invalid values (either 0 or 1).
                - warning_data (dict): A dictionary with warning data if the
                    value is invalid, including the warning message,
                    the actual value, and a detailed message.
        """
        valid = 0
        invalid = 0
        warning_data = {}

        if float_data > value:
            valid = 1
        else:
            invalid = 1
            warning_data = create_warning_data(
                float_data, f"Value should be greater than {value}"
            )

        return valid, invalid, warning_data

    @staticmethod
    def check_greater_than_equal(float_data: float, value: float) -> tuple:
        """
        check_greater_than_equal method.

        Check if a given float value is greater than or equal
        a specified value.

        Args:
            float_data (float): The float value to be checked.
            value (float): The specified value to compare against.

        Returns:
            tuple: A tuple containing the following elements:
                - valid (float): The number of valid values (either 0 or 1).
                - invalid(float): The number of invalid values (either 0 or 1).
                - warning_data (dict): A dictionary with warning data if the
                    value is invalid, including the warning message,
                    the actual value, and a detailed message.
        """
        valid = 0
        invalid = 0
        warning_data = {}

        if float_data >= value:
            valid = 1
        else:
            invalid = 1
            warning_data = create_warning_data(
                float_data, f"Value should be greater than equal {value}"
            )

        return valid, invalid, warning_data

    @staticmethod
    def check_in_range(
        float_data, lower_limit: float, upper_limit: float
    ) -> tuple:
        """
        Check if a given float value is within a specified range.

        Args:
            float_data (float): The float value to be checked.
            lower_limit (float): The lower limit of the range.
            upper_limit (float): The upper limit of the range.

        Returns:
            tuple: A tuple containing the following elements:
                - valid (float): The number of valid values (either 0 or 1).
                - invalid(float): The number of invalid values (either 0 or 1).
                - warning_data (dict): A dictionary with warning data if the
                    value is invalid, including the warning message,
                    the actual value, and a detailed message.
        """
        valid = 0
        invalid = 0
        warning_data = {}

        if float_data >= lower_limit and float_data <= upper_limit:
            valid = 1
        else:
            invalid = 1
            warning_data = create_warning_data(
                float_data,
                "Value should be in the range of "
                f"{lower_limit} and {upper_limit}",
            )

        return valid, invalid, warning_data

    @staticmethod
    def check_is_in(float_data: float, value: list) -> tuple:
        """
        check_is_in method.

        Check if a given float value is present in a specified
            list of values.

        Args:
            float_data (float): The float value to be checked.
            value (list): The list of values to check against.

        Returns:
            tuple: A tuple containing the following elements:
                - valid (float): The number of valid values (either 0 or 1).
                - invalid(float): The number of invalid values (either 0 or 1).
                - warning_data (dict): A dictionary with warning data if the
                    value is invalid, including the warning message,
                    the actual value, and a detailed message.
        """
        valid = 0
        invalid = 0
        warning_data = {}

        if float_data in value:
            valid = 1
        else:
            invalid = 1
            warning_data = create_warning_data(
                float_data, f"Value should be in {value}"
            )

        return valid, invalid, warning_data

    @staticmethod
    def check_not_in(float_data: float, value: list) -> tuple:
        """
        check_not_in method.

        Check if a given float value is not present in a specified
            list of values.

        Args:
            float_data (float): The float value to be checked.
            value (list): The list of values to check against.

        Returns:
            tuple: A tuple containing the following elements:
                - valid (float): The number of valid values (either 0 or 1).
                - invalid(float): The number of invalid values (either 0 or 1).
                - warning_data (dict): A dictionary with warning data if the
                    value is invalid, including the warning message,
                    the actual value, and a detailed message.
        """
        valid = 0
        invalid = 0
        warning_data = {}

        if float_data not in value:
            valid = 1
        else:
            invalid = 1
            warning_data = create_warning_data(
                float_data, f"Value should be not in {value}"
            )

        return valid, invalid, warning_data

    def equal_to(self, value: float, column: str) -> dict:
        """
        equal_to method.

        Check if the values in a specified column of a DataFrame are equal to
            a given value.

        Args:
            value (float): The value to compare the column values against.
            column (str): The name of the column in the DataFrame to check.

        Returns:
            dict: A dictionary containing the result of the data quality check,
                including the number of valid and invalid values,
                and any warning messages.
        """
        valid = 0
        invalid = 0
        warning = {}

        for index, float_data in enumerate(self.dataFrame[column]):
            try:
                if isinstance(float_data, (float)) is False:
                    raise InvalidDataTypeWarning(warning)

                valid_row, invalid_row, warning_data = self.check_equal(
                    float_data, value
                )
                valid += valid_row
                invalid += invalid_row

                if warning_data != {}:
                    warning[index] = InvalidDataValueWarning(
                        warning_data
                    ).message
            except InvalidDataTypeWarning:
                invalid += 1
                warning_data = create_warning_data(
                    float_data,
                    WarningDataDetailMessage.FLOAT_DATA_TYPE,
                    WarningDataMessage.INVALID_DATA_TYPE,
                )
                warning[index] = InvalidDataTypeWarning(warning_data).message

        result = self.response(valid, invalid, warning)
        return result

    def less_than(self, value: float, column: str) -> dict:
        """
        less_than method.

        Check if the values in a specified column of a DataFrame are less than
            a given value.

        Args:
            value (float): The value to compare the column values against.
            column (str): The name of the column in the DataFrame to check.

        Returns:
            dict: A dictionary containing the result of the data quality check,
                including the number of valid and invalid values,
                and any warning messages.
        """
        valid = 0
        invalid = 0
        warning = {}

        for index, float_data in enumerate(self.dataFrame[column]):
            try:
                if isinstance(float_data, (float)) is False:
                    raise InvalidDataTypeWarning(warning)
                valid_row, invalid_row, warning_data = self.check_less_than(
                    float_data, value
                )
                valid += valid_row
                invalid += invalid_row

                if warning_data != {}:
                    warning[index] = InvalidDataValueWarning(
                        warning_data
                    ).message
            except InvalidDataTypeWarning:
                invalid += 1
                warning_data = create_warning_data(
                    float_data,
                    WarningDataDetailMessage.FLOAT_DATA_TYPE,
                    WarningDataMessage.INVALID_DATA_TYPE,
                )
                warning[index] = InvalidDataTypeWarning(warning_data).message
        result = self.response(valid, invalid, warning)
        return result

    def less_than_equal(self, value: float, column: str) -> dict:
        """
        less_than_equal method.

        Check if the values in a specified column of a DataFrame are less than
            or equal to a given value.

        Args:
            value (float): The value to compare the column values against.
            column (str): The name of the column in the DataFrame to check.

        Returns:
            dict: A dictionary containing the result of the data quality check,
                including the number of valid and invalid values,
                and any warning messages.
        """
        valid = 0
        invalid = 0
        warning = {}

        for index, float_data in enumerate(self.dataFrame[column]):
            try:
                if isinstance(float_data, (float)) is False:
                    raise InvalidDataTypeWarning(warning)
                valid_row, invalid_row, warning_data = (
                    self.check_less_than_equal(float_data, value)
                    )
                valid += valid_row
                invalid += invalid_row

                if warning_data != {}:
                    warning[index] = InvalidDataValueWarning(
                        warning_data
                    ).message
            except InvalidDataTypeWarning:
                invalid += 1
                warning_data = create_warning_data(
                    float_data,
                    WarningDataDetailMessage.FLOAT_DATA_TYPE,
                    WarningDataMessage.INVALID_DATA_TYPE,
                )
                warning[index] = InvalidDataTypeWarning(warning_data).message

        result = self.response(valid, invalid, warning)
        return result

    def greater_than(self, value: float, column: str) -> dict:
        """
        greater_than method.

        Check if the values in a specified column of a DataFrame are
            greater than a given value.

        Args:
            value (float): The value to compare the column values against.
            column (str): The name of the column in the DataFrame to check.

        Returns:
            dict: A dictionary containing the result of the data quality check,
                including the number of valid and invalid values,
                and any warning messages.
        """
        valid = 0
        invalid = 0
        warning = {}

        for index, float_data in enumerate(self.dataFrame[column]):
            try:
                if isinstance(float_data, (float)) is False:
                    raise InvalidDataTypeWarning(warning)
                valid_row, invalid_row, warning_data = self.check_greater_than(
                    float_data, value
                )
                valid += valid_row
                invalid += invalid_row

                if warning_data != {}:
                    warning[index] = InvalidDataValueWarning(
                        warning_data
                    ).message
            except InvalidDataTypeWarning:
                invalid += 1
                warning_data = create_warning_data(
                    float_data,
                    WarningDataDetailMessage.FLOAT_DATA_TYPE,
                    WarningDataMessage.INVALID_DATA_TYPE,
                )
                warning[index] = InvalidDataTypeWarning(warning_data).message

        result = self.response(valid, invalid, warning)
        return result

    def greater_than_equal(self, value: float, column: str) -> dict:
        """
        greater_than_equal method.

        Checks if the values in a specified column of a DataFrame are
            greater than or equal to a given value.

        Args:
            value (float): The value to compare the column values against.
            column (str): The name of the column in the DataFrame to check.

        Returns:
            dict: A dictionary containing the result of the data quality check,
                including the number of valid and invalid values,
                and any warning messages.
        """
        valid = 0
        invalid = 0
        warning = {}

        for index, float_data in enumerate(self.dataFrame[column]):
            try:
                if isinstance(float_data, (float)) is False:
                    raise InvalidDataTypeWarning(warning)

                (
                    valid_row,
                    invalid_row,
                    warning_data,
                ) = self.check_greater_than_equal(float_data, value)
                valid += valid_row
                invalid += invalid_row

                if warning_data != {}:
                    warning[index] = InvalidDataValueWarning(
                        warning_data
                    ).message
            except InvalidDataTypeWarning:
                invalid += 1
                warning_data = create_warning_data(
                    float_data,
                    WarningDataDetailMessage.FLOAT_DATA_TYPE,
                    WarningDataMessage.INVALID_DATA_TYPE,
                )
                warning[index] = InvalidDataTypeWarning(warning_data).message

        result = self.response(valid, invalid, warning)
        return result

    def in_range(
        self, lower_limit: float, upper_limit: float, column: str
    ) -> dict:
        """
        in_range method.

        Check if the values in a specified column of a DataFrame are within
            a given range.

        Args:
            lower_limit (float): The lower limit of the range to check against.
            upper_limit (float): The upper limit of the range to check against.
            column (str): The name of the column in the DataFrame to check.

        Returns:
            dict: A dictionary containing the result of the data quality check,
                including the number of valid and invalid values,
                and any warning messages.
        """
        valid = 0
        invalid = 0
        warning = {}

        for index, float_data in enumerate(self.dataFrame[column]):
            try:
                if isinstance(float_data, (float)) is False:
                    raise InvalidDataTypeWarning(warning)
                valid_row, invalid_row, warning_data = self.check_in_range(
                    float_data, lower_limit, upper_limit
                )
                valid += valid_row
                invalid += invalid_row

                if warning_data != {}:
                    warning[index] = InvalidDataValueWarning(
                        warning_data
                    ).message
            except InvalidDataTypeWarning:
                invalid += 1
                warning_data = create_warning_data(
                    float_data,
                    WarningDataDetailMessage.FLOAT_DATA_TYPE,
                    WarningDataMessage.INVALID_DATA_TYPE,
                )
                warning[index] = InvalidDataTypeWarning(warning_data).message

        result = self.response(valid, invalid, warning)
        return result

    def is_in(self, value: list, column: str) -> dict:
        """
        is_in method.

        Check if the values in a specified column of a DataFrame are present
            in a given list of values.

        Args:
            value (list): A list of values to check against.
            column (str): The name of the column in the DataFrame to check.

        Returns:
            dict: A dictionary containing the result of the data quality check,
                including the number of valid and invalid values,
                and any warning messages.
        """
        valid = 0
        invalid = 0
        warning = {}

        for index, float_data in enumerate(self.dataFrame[column]):
            try:
                if isinstance(float_data, (float)) is False:
                    raise InvalidDataTypeWarning(warning)

                valid_row, invalid_row, warning_data = self.check_is_in(
                    float_data, value
                )
                valid += valid_row
                invalid += invalid_row

                if warning_data != {}:
                    warning[index] = InvalidDataValueWarning(
                        warning_data
                    ).message
            except InvalidDataTypeWarning:
                invalid += 1
                warning_data = create_warning_data(
                    float_data,
                    WarningDataDetailMessage.FLOAT_DATA_TYPE,
                    WarningDataMessage.INVALID_DATA_TYPE,
                )
                warning[index] = InvalidDataTypeWarning(warning_data).message

        result = self.response(valid, invalid, warning)
        return result

    def not_in(self, value: list, column: str) -> dict:
        """
        not_in method.

        Checks if the values in a specified column of a DataFrame are not
            present in a given list of values.

        Args:
            value (list): A list of values to check against the column values.
            column (str): The name of the column in the DataFrame to check.

        Returns:
            dict: A dictionary containing the result of the data quality check,
                including the number of valid and invalid values,
                and any warning messages.
        """
        valid = 0
        invalid = 0
        warning = {}

        for index, float_data in enumerate(self.dataFrame[column]):
            try:
                if isinstance(float_data, (float)) is False:
                    raise InvalidDataTypeWarning(warning)
                valid_row, invalid_row, warning_data = self.check_not_in(
                    float_data, value
                )
                valid += valid_row
                invalid += invalid_row

                if warning_data != {}:
                    warning[index] = InvalidDataValueWarning(
                        warning_data
                    ).message
            except InvalidDataTypeWarning:
                invalid += 1
                warning_data = create_warning_data(
                    float_data,
                    WarningDataDetailMessage.FLOAT_DATA_TYPE,
                    WarningDataMessage.INVALID_DATA_TYPE,
                )
                warning[index] = InvalidDataTypeWarning(warning_data).message

        result = self.response(valid, invalid, warning)
        return result

#!/usr/bin/env python3

# Copyright (C) Free Software Foundation, Inc. All rights reserved.
# Licensed under the AGPL-3.0-only License. See LICENSE in the project root
# for license information.

"""Library data quality for boolean type."""

import pandas as pd

from .exception import InvalidDataTypeWarning
from .utils import Basic, create_warning_data, WarningDataMessage


class WarningDataDetailMessage:
    """
    Provides predefined error messages for specific data validation scenarios.

    Attributes:
        BOOLEAN_DATA_TYPE (str): Error message for the scenario when a value
            must be of boolean data type.
        DEFINED_DATA_TYPE (str): Error message for the scenario when a value
            must be equal to a defined value.
    """

    BOOLEAN_DATA_TYPE: str = "Value must be of boolean data type"
    DEFINED_DATA_TYPE: str = "Value must be equal to defined value"


class Boolean(Basic):
    """Data Quality class for boolean type."""

    def __init__(self, dataFrame: pd.DataFrame):
        """
        Instance initialitzation of the Integer class.

        Args:
            dataFrame (pd.DataFrame): The data you want to process.
        """
        self.dataFrame = dataFrame

    @staticmethod
    def check_bool(bool_data: bool) -> tuple:
        """
        Check if every row of a given DataFrame column is Boolean data type.

        Args:
            bool_data (bool): The boolean value to be checked.

        Returns:
            tuple: A tuple containing the following elements:
                - valid (int): The number of valid values (either 0 or 1).
                - invalid (int): The number of invalid values (either 0 or 1).
                - warning_data (dict): A dictionary with warning data if the
                    value is invalid, including the warning message,
                    the actual value, and a detailed message.
        """
        valid = 0
        invalid = 0
        warning_data = {}

        if isinstance(bool_data, bool):
            valid = 1
        # else:
        #     invalid = 1
        #     warning_data = create_warning_data(
        #         bool_data, "Value should be boolean"
        #     )

        return valid, invalid, warning_data

    def is_bool(self, column: str) -> dict:
        """
        Checker method for boolean type data.

        Check if the value in a specified column of a DataFrame
            are boolean data type.

        Args:
            column (str): The name of the column in the DataFrame to check

        Returns:
            dict: A dictionary containing the result of the data quality check,
                including the number of valid and invalid values,
                and any warning messages.
        """
        valid = 0
        invalid = 0
        warning = {}

        for index, bool_data in enumerate(self.dataFrame[column]):
            try:
                if isinstance(bool_data, (bool)) is False:
                    raise InvalidDataTypeWarning(warning)

                valid_row, invalid_row, warning_data = self.check_bool(
                    bool_data
                )
                valid += valid_row
                invalid += invalid_row

                # if warning_data != {}:
                #     warning[index] = InvalidDataValueWarning(
                #         warning_data
                #     ).message
            except InvalidDataTypeWarning:
                invalid += 1
                warning_data = create_warning_data(
                    bool_data,
                    WarningDataDetailMessage.BOOLEAN_DATA_TYPE,
                    WarningDataMessage.INVALID_DATA_TYPE,
                )
                warning[index] = InvalidDataTypeWarning(warning_data).message

        result = self.response(valid, invalid, warning)
        return result

    @staticmethod
    def check_is_in(bool_data, is_in: list):
        """
        Checker in method for boolean type data.

        Check if every row of a given DataFrame column are equal to
            defined boolean list.

        Args:
            bool_data (_type_): the boolean value to be checked.
            is_in (list): Defined boolean list other than True or False.
                for example: [1, 0], ['Ya', 'Tidak'], ['Benar', 'Salah'], etc.

        Returns:
            tuple: A tuple containing the following elements:
                - valid (int): The number of valid values (either 0 or 1).
                - invalid (int): The number of invalid values (either 0 or 1).
                - warning_data (dict): A dictionary with warning data if the
                    value is invalid, including the warning message,
                    the actual value, and a detailed message.
        """
        valid = 0
        invalid = 0
        warning_data = {}

        if bool_data in is_in:
            valid = 1
        # else:
        #     invalid = 1
        #     warning_data = create_warning_data(
        #         bool_data, "Value should be equal to defined list"
        #     )

        return valid, invalid, warning_data

    def is_in(self, is_in: list, column: str) -> dict:
        """
        Checker in method for boolean type data.

        Check if every row of a given DataFrame column are equal to
            defined boolean list

        Args:
            is_in (list): Defined boolean list other than True or False.
                for example: [1, 0], ['Ya', 'Tidak'], ['Benar', 'Salah'], etc.
            column (str): The name of the column in the DataFrame to check

        Returns:
            dict: A dictionary containing the result of the data quality check,
                including the number of valid and invalid values,
                and any warning messages.
        """
        valid = 0
        invalid = 0
        warning = {}

        for index, bool_data in enumerate(self.dataFrame[column]):
            try:
                if bool_data not in is_in:
                    raise InvalidDataTypeWarning(warning)

                valid_row, invalid_row, warning_data = self.check_is_in(
                    bool_data, is_in
                )
                valid += valid_row
                invalid += invalid_row

                # if warning_data != {}:
                #     warning[index] = InvalidDataValueWarning(
                #         warning_data
                #     ).message
            except InvalidDataTypeWarning:
                invalid += 1
                warning_data = create_warning_data(
                    bool_data,
                    WarningDataDetailMessage.DEFINED_DATA_TYPE,
                    WarningDataMessage.INVALID_DATA_TYPE,
                )
                warning[index] = InvalidDataTypeWarning(warning_data).message

        result = self.response(valid, invalid, warning)
        return result

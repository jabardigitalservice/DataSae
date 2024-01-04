# !/usr/bin/env python3

# Copyright (C) Free Software Foundation, Inc. All rights reserved.
# Licensed under the AGPL-3.0-only License. See LICENSE in the project root
# for license information.

"""String library."""

import re

import pandas as pd

from .exception import InvalidDataTypeWarning, InvalidDataValueWarning
from .utils import Basic, create_warning_data, WarningDataMessage


class WarningDataDetailMessage:
    """WarningDataDetailMessage class."""

    STRING_DATA_TYPE: str = "Value must be of string data type"


class String(Basic):
    """String class."""

    def __init__(self, dataFrame: pd.DataFrame):
        """
        __init__ method.

        Initializes an instance of the String class.

        Args:
            dataFrame (pd.DataFrame): The data you want to process.
        """
        self.dataFrame = dataFrame

    @staticmethod
    def check_contain(string_data: str, compare_data: str) -> tuple:
        """
        check_contain method.

        Check if a given string value is not present in a specified
            dict

        Args:
            string_data (str): The string value to be checked.
            compare_data: The list of values to check against.

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
        if string_data in compare_data:
            valid = 1
        else:
            invalid = 1
            warning_data = create_warning_data(
                compare_data,
                f"Value should be contain to {string_data}",
            )

        return valid, invalid, warning_data

    @staticmethod
    def check_not_contain(string_data: str, compare_data: str) -> tuple:
        """
        check_not_contain method.

        Check if a given string value is not present in a specified
            dict

        Args:
            string_data (str): The string value to be checked.
            compare_data: The list of values to check against.

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
        if string_data not in compare_data:
            valid = 1
        else:
            invalid = 1
            warning_data = create_warning_data(
                compare_data,
                f"Value should be not contain to {string_data}",
            )

        return valid, invalid, warning_data

    @staticmethod
    def check_regex_contain(regex_data: str, compare_data: str) -> tuple:
        """
        check_regex_contain method.

        Check if a given regex string value is not present in a specified
            dict

        Args:
            regex_data (str): The string regex value to be checked.
            compare_data: The list of values to check against.

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
        regexp = re.compile(r"{}".format(regex_data))
        if regexp.search(compare_data):
            valid = 1
        else:
            invalid = 1
            warning_data = create_warning_data(
                compare_data,
                f"Value should be contain to {regex_data}",
            )

        return valid, invalid, warning_data

    @staticmethod
    def check_special_char_contain(char: str, compare_data: str) -> tuple:
        """
        check_special_char_contain method.

        Check if a given character value is present in a specified
            dict

        Args:
            char (str): The string char value to be checked.
            compare_data: The list of values to check against.

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
        punctuation = """[!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"""
        if char in punctuation:
            if char in compare_data:
                valid = 1
            else:
                invalid = 1
                warning_data = create_warning_data(
                    compare_data,
                    f"Value should be contain to {char}",
                )

        return valid, invalid, warning_data

    @staticmethod
    def check_is_uppercase(str_data: str) -> tuple:
        """
        check_is_uppercase method.

        Check if given character is all uppercase or not

        Args:
            str_data (str): The string char value to be checked.

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
        if str_data.isupper():
            valid = 1
        else:
            invalid = 1
            warning_data = create_warning_data(
                str_data, "Value should uppercase"
            )

        return valid, invalid, warning_data

    @staticmethod
    def check_is_lowercase(str_data: str) -> tuple:
        """
        check_is_lowercase method.

        Check if given character is all lower case or not

        Args:
            str_data (str): The string char value to be checked.

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
        if str_data.islower():
            valid = 1
        else:
            invalid = 1
            warning_data = create_warning_data(
                str_data, "Value should lowercase"
            )

        return valid, invalid, warning_data

    @staticmethod
    def check_is_capitalize_first_word(str_data: str) -> tuple:
        """
        check_is_capitalize_first_word method.

        Check if given character is capitalize in first word

        Args:
            str_data (str): The string char value to be checked.

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
        if str_data.strip()[0].isupper():
            valid = 1
        else:
            invalid = 1
            warning_data = create_warning_data(
                str_data, "Value should capitalize first word"
            )

        return valid, invalid, warning_data

    @staticmethod
    def check_is_capitalize_all_word(str_data: str) -> tuple:
        """
        check_is_capitalize_all_word method.

        Check if given character is capitalize in all word

        Args:
            str_data (str): The string char value to be checked.

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
        if str_data.istitle():
            valid = 1
        else:
            invalid = 1
            warning_data = create_warning_data(
                str_data, "Value should capitalize all word"
            )

        return valid, invalid, warning_data

    def contain(self, str_contain, column) -> dict:
        """
        Contain method.

        data quality for string contain.

        Args:
            str_contain: string that want to check
            column: column name that want to check

        Returns:
            dict: A dictionary containing the result of the data quality check,
                including the number of valid and invalid values,
                and any warning messages.
        """
        valid = 0
        invalid = 0
        warning = {}

        for index, str_data in enumerate(self.dataFrame[column]):
            try:
                if isinstance(str_data, (str)) is False:
                    raise InvalidDataTypeWarning(warning)
                valid_row, invalid_row, warning_data = self.check_contain(
                    str_contain, str_data
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
                    str_data,
                    WarningDataDetailMessage.STRING_DATA_TYPE,
                    WarningDataMessage.INVALID_DATA_TYPE,
                )
                warning[index] = InvalidDataTypeWarning(warning_data).message
        result = self.response(valid, invalid, warning)
        return result

    def not_contain(self, str_not_contain, column):
        """
        not_contain method.

        data quality for string not contain.

        Args:
            str_not_contain (str): The string char value to be checked.
            column: column name of the data

        Returns:
            dict: A dictionary containing the result of the data quality check,
                including the number of valid and invalid values,
                and any warning messages.
        """
        valid = 0
        invalid = 0
        warning = {}

        for index, str_data in enumerate(self.dataFrame[column]):
            try:
                if isinstance(str_data, (str)) is False:
                    raise InvalidDataTypeWarning(warning)
                valid_row, invalid_row, warning_data = self.check_not_contain(
                    str_not_contain, str_data
                )
                valid += valid_row
                invalid += invalid_row
                if warning_data != {}:
                    warning[index] = InvalidDataValueWarning(
                        warning_data
                    ).message
            except InvalidDataTypeWarning:
                invalid += 1
                warning_data = warning_data = create_warning_data(
                    str_data,
                    WarningDataDetailMessage.STRING_DATA_TYPE,
                    WarningDataMessage.INVALID_DATA_TYPE,
                )
                warning[index] = InvalidDataTypeWarning(warning_data).message
        result = self.response(valid, invalid, warning)
        return result

    def regex_contain(self, regex_data, column) -> dict:
        """
        regex_contain method.

        data quality for regex contain.

        Args:
            regex_data: regex string that want to check
            column: column name that want to check

        Returns:
            dict: A dictionary containing the result of the data quality check,
                including the number of valid and invalid values,
                and any warning messages.
        """
        valid = 0
        invalid = 0
        warning = {}

        for index, str_data in enumerate(self.dataFrame[column]):
            try:
                if isinstance(str_data, (str)) is False:
                    raise InvalidDataTypeWarning(warning)
                (
                    valid_row,
                    invalid_row,
                    warning_data,
                ) = self.check_regex_contain(regex_data, str_data)
                valid += valid_row
                invalid += invalid_row
                if warning_data != {}:
                    warning[index] = InvalidDataValueWarning(
                        warning_data
                    ).message
            except InvalidDataTypeWarning:
                invalid += 1
                warning_data = create_warning_data(
                    str_data,
                    WarningDataDetailMessage.STRING_DATA_TYPE,
                    WarningDataMessage.INVALID_DATA_TYPE,
                )
                warning[index] = InvalidDataTypeWarning(warning_data).message
        result = self.response(valid, invalid, warning)
        return result

    def special_char_contain(self, char, column) -> dict:
        """
        special_char_contain method.

        data quality for special char contain.

        Args:
            char: char string that want to check
            column: column name that want to check

        Returns:
            dict: A dictionary containing the result of the data quality check,
                including the number of valid and invalid values,
                and any warning messages.
        """
        valid = 0
        invalid = 0
        warning = {}

        for index, str_data in enumerate(self.dataFrame[column]):
            try:
                if isinstance(str_data, (str)) is False:
                    raise InvalidDataTypeWarning(warning)
                (
                    valid_row,
                    invalid_row,
                    warning_data,
                ) = self.check_special_char_contain(char, str_data)
                valid += valid_row
                invalid += invalid_row
                if warning_data != {}:
                    warning[index] = InvalidDataValueWarning(
                        warning_data
                    ).message
            except InvalidDataTypeWarning:
                invalid += 1
                warning_data = create_warning_data(
                    str_data,
                    WarningDataDetailMessage.STRING_DATA_TYPE,
                    WarningDataMessage.INVALID_DATA_TYPE,
                )
                warning[index] = InvalidDataTypeWarning(warning_data).message
        result = self.response(valid, invalid, warning)
        return result

    def is_uppercase(self, column) -> dict:
        """
        is_uppercase method.

        data quality for check in column is uppercase

        Args:
            column: column name of df that want to check

        Returns:
            dict: A dictionary containing the result of the data quality check,
                including the number of valid and invalid values,
                and any warning messages.
        """
        valid = 0
        invalid = 0
        warning = {}

        for index, str_data in enumerate(self.dataFrame[column]):
            try:
                if isinstance(str_data, (str)) is False:
                    raise InvalidDataTypeWarning(warning)
                valid_row, invalid_row, warning_data = self.check_is_uppercase(
                    str_data
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
                    str_data,
                    WarningDataDetailMessage.STRING_DATA_TYPE,
                    WarningDataMessage.INVALID_DATA_TYPE,
                )
                warning[index] = InvalidDataTypeWarning(warning_data).message
        result = self.response(valid, invalid, warning)
        return result

    def is_lowercase(self, column) -> dict:
        """
        is_lowercase method.

        data quality for check in column is lower case

        Args:
            column: column name of df that want to check

        Returns:
            dict: A dictionary containing the result of the data quality check,
                including the number of valid and invalid values,
                and any warning messages.
        """
        valid = 0
        invalid = 0
        warning = {}

        for index, str_data in enumerate(self.dataFrame[column]):
            try:
                if isinstance(str_data, (str)) is False:
                    raise InvalidDataTypeWarning(warning)
                valid_row, invalid_row, warning_data = self.check_is_lowercase(
                    str_data
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
                    str_data,
                    WarningDataDetailMessage.STRING_DATA_TYPE,
                    WarningDataMessage.INVALID_DATA_TYPE,
                )
                warning[index] = InvalidDataTypeWarning(warning_data).message
        result = self.response(valid, invalid, warning)
        return result

    def is_capitalize_first_word(self, column) -> dict:
        """
        is_capitalize_first_word method.

        data quality for check in column is capitalize in first word

        Args:
            column: column name of df that want to check

        Returns:
            dict: A dictionary containing the result of the data quality check,
                including the number of valid and invalid values,
                and any warning messages.
        """
        valid = 0
        invalid = 0
        warning = {}

        for index, str_data in enumerate(self.dataFrame[column]):
            try:
                if isinstance(str_data, (str)) is False:
                    raise InvalidDataTypeWarning(warning)
                (
                    valid_row,
                    invalid_row,
                    warning_data,
                ) = self.check_is_capitalize_first_word(str_data)
                valid += valid_row
                invalid += invalid_row
                if warning_data != {}:
                    warning[index] = InvalidDataValueWarning(
                        warning_data
                    ).message
            except InvalidDataTypeWarning:
                invalid += 1
                warning_data = create_warning_data(
                    str_data,
                    WarningDataDetailMessage.STRING_DATA_TYPE,
                    WarningDataMessage.INVALID_DATA_TYPE,
                )
                warning[index] = InvalidDataTypeWarning(warning_data).message
        result = self.response(valid, invalid, warning)
        return result

    def is_capitalize_all_word(self, column) -> dict:
        """
        is_capitalize_all_word method.

        data quality for check in column is capitalize in all word

        Args:
            column: column name of df that want to check

        Returns:
            dict: A dictionary containing the result of the data quality check,
                including the number of valid and invalid values,
                and any warning messages.
        """
        valid = 0
        invalid = 0
        warning = {}

        for index, str_data in enumerate(self.dataFrame[column]):
            try:
                if isinstance(str_data, (str)) is False:
                    raise InvalidDataTypeWarning(warning)
                (
                    valid_row,
                    invalid_row,
                    warning_data,
                ) = self.check_is_capitalize_all_word(str_data)
                valid += valid_row
                invalid += invalid_row
                if warning_data != {}:
                    warning[index] = InvalidDataValueWarning(
                        warning_data
                    ).message
            except InvalidDataTypeWarning:
                invalid += 1
                warning_data = create_warning_data(
                    str_data,
                    WarningDataDetailMessage.STRING_DATA_TYPE,
                    WarningDataMessage.INVALID_DATA_TYPE,
                )
                warning[index] = InvalidDataTypeWarning(warning_data).message
        result = self.response(valid, invalid, warning)
        return result

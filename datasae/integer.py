#!/usr/bin/env python3

# This module is part of DataSae and is released under
# the AGPL-3.0-only License: https://opensource.org/license/agpl-v3/


from .exception import InvalidDataTypeWarning, InvalidDataValueWarning
from .utils import Basic
import pandas as pd


class Integer(Basic):
    def __init__(self, dataFrame: pd.DataFrame):
        """
        Class Init

        Args:
            dataFrame (pd.DataFrame): The data you want to process
        """
        self.dataFrame = dataFrame

    @staticmethod
    def check_equal(integer_data: int, value: int):
        valid = 0
        invalid = 0
        warning_data = dict()
        if integer_data == value:
            valid = 1
        else:
            invalid = 1
            warning_data = {
                "message": "Invalid Value",
                "value": integer_data,
                "detail_message": (f"Value should be equal to {value}"),
            }
        return valid, invalid, warning_data

    @staticmethod
    def check_less_then(integer_data: int, value: int):
        valid = 0
        invalid = 0
        warning_data = dict()
        if integer_data < value:
            valid = 1
        else:
            invalid = 1
            warning_data = {
                "message": "Invalid Value",
                "value": integer_data,
                "detail_message": (f"Value should be less then {value}"),
            }
        return valid, invalid, warning_data

    @staticmethod
    def check_less_then_equal(integer_data: int, value: int):
        valid = 0
        invalid = 0
        warning_data = dict()
        if integer_data <= value:
            valid = 1
        else:
            invalid = 1
            warning_data = {
                "message": "Invalid Value",
                "value": integer_data,
                "detail_message": (f"Value should be less then equal {value}"),
            }
        return valid, invalid, warning_data

    @staticmethod
    def check_greater_then(integer_data: int, value: int):
        valid = 0
        invalid = 0
        warning_data = dict()
        if integer_data > value:
            valid = 1
        else:
            invalid = 1
            warning_data = {
                "message": "Invalid Value",
                "value": integer_data,
                "detail_message": (f"Value should be greater then {value}"),
            }
        return valid, invalid, warning_data

    @staticmethod
    def check_greater_then_equal(integer_data: int, value: int):
        valid = 0
        invalid = 0
        warning_data = dict()
        if integer_data >= value:
            valid = 1
        else:
            invalid = 1
            warning_data = {
                "message": "Invalid Value",
                "value": integer_data,
                "detail_message": (
                    f"Value should be greater_then_equal {value}"
                ),
            }
        return valid, invalid, warning_data

    @staticmethod
    def check_in_range(integer_data, lower_limit: int, upper_limit: int):
        valid = 0
        invalid = 0
        warning_data = dict()
        if integer_data >= lower_limit and integer_data <= upper_limit:
            valid = 1
        else:
            invalid = 1
            warning_data = {
                "message": "Invalid Value",
                "value": integer_data,
                "detail_message": (
                    "Value should be in the range of "
                    f"{lower_limit} and {upper_limit}"
                ),
            }
        return valid, invalid, warning_data

    @staticmethod
    def check_is_in(integer_data: int, value: list):
        valid = 0
        invalid = 0
        warning_data = dict()
        if integer_data in value:
            valid = 1
        else:
            invalid = 1
            warning_data = {
                "message": "Invalid Value",
                "value": integer_data,
                "detail_message": f"Value should be in {value}",
            }
        return valid, invalid, warning_data

    @staticmethod
    def check_not_in(integer_data: int, value: list):
        valid = 0
        invalid = 0
        warning_data = dict()
        if integer_data not in value:
            valid = 1
        else:
            invalid = 1
            warning_data = {
                "message": "Invalid Value",
                "value": integer_data,
                "detail_message": f"Value should be not in {value}",
            }
        return valid, invalid, warning_data

    @staticmethod
    def check_length(integer_data: int, value: list):
        valid = 0
        invalid = 0
        warning_data = dict()
        if len(integer_data) == value:
            valid = 1
        else:
            invalid = 1
            warning_data = {
                "message": "Invalid Value",
                "value": integer_data,
                "detail_message": f"Value should have a length of {value}",
            }
        return valid, invalid, warning_data

    def equal_to(self, value: int, column: str) -> dict:
        """
        Equal value to columns

        Args:
            value (int): Number Equal to
            column (str): Name column from dataframe

        Raises:
            InvalidDataTypeWarning: invalid data type response

        Returns:
            dict: result score data quality
        """

        valid = 0
        invalid = 0
        warning = dict()

        for index, integer_data in enumerate(self.dataFrame[column]):
            try:
                if isinstance(integer_data, (int)) is False:
                    raise InvalidDataTypeWarning(warning)

                valid, invalid, warning_data = self.check_equal(
                    integer_data, value
                )
                valid += valid
                invalid += invalid
                warning[index] = InvalidDataValueWarning(warning_data).message
            except InvalidDataTypeWarning:
                invalid += 1
                warning_data = {
                    "message": "Invalid Data Type",
                    "value": integer_data,
                    "detail_message": "Value must be of integer data type",
                }
                warning[index] = InvalidDataTypeWarning(warning_data).message

        result = self.response(valid, invalid, warning)
        return result

    def less_then(self, value: int, column: str) -> dict:
        """
        Less than value to columns

        Args:
            value (int): Number Less then
            column (str): Name column from dataframe

        Raises:
            InvalidDataTypeWarning: invalid data type response

        Returns:
            dict: result score data quality
        """

        valid = 0
        invalid = 0
        warning = dict()

        for index, integer_data in enumerate(self.dataFrame[column]):
            try:
                if isinstance(integer_data, (int)) is False:
                    raise InvalidDataTypeWarning(warning)
                valid, invalid, warning_data = self.check_less_then(
                    integer_data, value
                )
                valid += valid
                invalid += invalid
                warning[index] = InvalidDataValueWarning(warning_data).message
            except InvalidDataTypeWarning:
                invalid += 1
                warning_data = {
                    "message": "Invalid Data Type",
                    "value": integer_data,
                    "detail_message": "Value must be of integer data type",
                }
                warning[index] = InvalidDataTypeWarning(warning_data).message

        result = self.response(valid, invalid, warning)
        return result

    def less_then_equal(self, value: int, column: str) -> dict:
        """
        Less than or equal value to columns

        Args:
            value (int): Number Less than or equal
            column (str): Name column from dataframe

        Raises:
            InvalidDataTypeWarning: invalid data type response

        Returns:
            dict: result score data quality
        """

        valid = 0
        invalid = 0
        warning = dict()

        for index, integer_data in enumerate(self.dataFrame[column]):
            try:
                if isinstance(integer_data, (int)) is False:
                    raise InvalidDataTypeWarning(warning)
                valid, invalid, warning_data = self.check_less_then(
                    integer_data, value
                )
                valid += valid
                invalid += invalid
                warning[index] = InvalidDataValueWarning(warning_data).message
            except InvalidDataTypeWarning:
                invalid += 1
                warning_data = {
                    "message": "Invalid Data Type",
                    "value": integer_data,
                    "detail_message": "Value must be of integer data type",
                }
                warning[index] = InvalidDataTypeWarning(warning_data).message

        result = self.response(valid, invalid, warning)
        return result

    def greater_then(self, value: int, column: str) -> dict:
        """
        Greater than value to columns

        Args:
            value (int): Number greater than
            column (str): Name column from dataframe

        Raises:
            InvalidDataTypeWarning: invalid data type response

        Returns:
            dict: result score data quality
        """

        valid = 0
        invalid = 0
        warning = dict()

        for index, integer_data in enumerate(self.dataFrame[column]):
            try:
                if isinstance(integer_data, (int)) is False:
                    raise InvalidDataTypeWarning(warning)
                valid, invalid, warning_data = self.check_greater_then(
                    integer_data, value
                )
                valid += valid
                invalid += invalid
                warning[index] = InvalidDataValueWarning(warning_data).message
            except InvalidDataTypeWarning:
                invalid += 1
                warning_data = {
                    "message": "Invalid Data Type",
                    "value": integer_data,
                    "detail_message": "Value must be of integer data type",
                }
                warning[index] = InvalidDataTypeWarning(warning_data).message

        result = self.response(valid, invalid, warning)
        return result

    def greater_then_equal(self, value: int, column: str) -> dict:
        """
        Greater than or equal value to columns

        Args:
            value (int): Number greater than or equal
            column (str): Name column from dataframe

        Raises:
            InvalidDataTypeWarning: invalid data type response

        Returns:
            dict: result score data quality
        """

        valid = 0
        invalid = 0
        warning = dict()

        for index, integer_data in enumerate(self.dataFrame[column]):
            try:
                if isinstance(integer_data, (int)) is False:
                    raise InvalidDataTypeWarning(warning)
                valid, invalid, warning_data = self.check_greater_then_equal(
                    integer_data, value
                )
                valid += valid
                invalid += invalid
                warning[index] = InvalidDataValueWarning(warning_data).message
            except InvalidDataTypeWarning:
                invalid += 1
                warning_data = {
                    "message": "Invalid Data Type",
                    "value": integer_data,
                    "detail_message": "Value must be of integer data type",
                }
                warning[index] = InvalidDataTypeWarning(warning_data).message

        result = self.response(valid, invalid, warning)
        return result

    def in_range(
        self, lower_limit: int, upper_limit: int, column: str
    ) -> dict:
        """
        Range value to columns

        Args:
            lower_limit (int): Lower limit number in range
            upper_limit (int): Upper limit number in range
            column (str): Name column from dataframe

        Raises:
            InvalidDataTypeWarning: invalid data type response

        Returns:
            dict: result score data quality
        """

        valid = 0
        invalid = 0
        warning = dict()

        for index, integer_data in enumerate(self.dataFrame[column]):
            try:
                if isinstance(integer_data, (int)) is False:
                    raise InvalidDataTypeWarning(warning)
                valid, invalid, warning_data = self.check_in_range(
                    integer_data, lower_limit, upper_limit
                )
                valid += valid
                invalid += invalid
                warning[index] = InvalidDataValueWarning(warning_data).message
            except InvalidDataTypeWarning:
                invalid += 1
                warning_data = {
                    "message": "Invalid Data Type",
                    "value": integer_data,
                    "detail_message": "Value must be of integer data type",
                }
                warning[index] = InvalidDataTypeWarning(warning_data).message

        result = self.response(valid, invalid, warning)
        return result

    def is_in(self, value: list, column: str) -> dict:
        """
        Is in value to columns

        Args:
            value (list): Number inside list
            column (str): Name column from dataframe

        Raises:
            InvalidDataTypeWarning: invalid data type response

        Returns:
            dict: result score data quality
        """

        valid = 0
        invalid = 0
        warning = dict()

        for index, integer_data in enumerate(self.dataFrame[column]):
            try:
                if isinstance(integer_data, (int)) is False:
                    raise InvalidDataTypeWarning(warning)
                valid, invalid, warning_data = self.check_is_in(
                    integer_data, value
                )
                valid += valid
                invalid += invalid
                warning[index] = InvalidDataValueWarning(warning_data).message
            except InvalidDataTypeWarning:
                invalid += 1
                warning_data = {
                    "message": "Invalid Data Type",
                    "value": integer_data,
                    "detail_message": "Value must be of integer data type",
                }
                warning[index] = InvalidDataTypeWarning(warning_data).message

        result = self.response(valid, invalid, warning)
        return result

    def not_in(self, value: list, column: str) -> dict:
        """
        Not in value to columns

        Args:
            value (list): Number outside list
            column (str): Name column from dataframe

        Raises:
            InvalidDataTypeWarning: invalid data type response

        Returns:
            dict: result score data quality
        """

        valid = 0
        invalid = 0
        warning = dict()

        for index, integer_data in enumerate(self.dataFrame[column]):
            try:
                if isinstance(integer_data, (int)) is False:
                    raise InvalidDataTypeWarning(warning)
                valid, invalid, warning_data = self.check_not_in(
                    integer_data, value
                )
                valid += valid
                invalid += invalid
                warning[index] = InvalidDataValueWarning(warning_data).message
            except InvalidDataTypeWarning:
                invalid += 1
                warning_data = {
                    "message": "Invalid Data Type",
                    "value": integer_data,
                    "detail_message": "Value must be of integer data type",
                }
                warning[index] = InvalidDataTypeWarning(warning_data).message

        result = self.response(valid, invalid, warning)
        return result

    def length(self, value: int, column: str) -> dict:
        """
        Length of value to columns

        Args:
            value (list): Number of lenght
            column (str): Name column from dataframe

        Raises:
            InvalidDataTypeWarning: invalid data type response

        Returns:
            dict: result score data quality
        """

        valid = 0
        invalid = 0
        warning = dict()

        for index, integer_data in enumerate(self.dataFrame[column]):
            try:
                if isinstance(integer_data, (int)) is False:
                    raise InvalidDataTypeWarning(warning)
                valid, invalid, warning_data = self.check_length(
                    integer_data, value
                )
                valid += valid
                invalid += invalid
                warning[index] = InvalidDataValueWarning(warning_data).message
            except InvalidDataTypeWarning:
                invalid += 1
                warning_data = {
                    "message": "Invalid Data Type",
                    "value": integer_data,
                    "detail_message": "Value must be of integer data type",
                }
                warning[index] = InvalidDataTypeWarning(warning_data).message

        result = self.response(valid, invalid, warning)
        return result

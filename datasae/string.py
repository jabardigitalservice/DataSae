#!/usr/bin/env python3

# This module is part of DataSae and is released under
# the AGPL-3.0-only License: https://opensource.org/license/agpl-v3/


from exception import InvalidDataTypeWarning, InvalidDataValueWarning
from typing import Union
from utils import Basic
import pandas
import re
import string


class String(Basic):
    def __init__(self, dataFrame: pandas.DataFrame):
        """
        Initializes an instance of the String class.

        Args:
            dataFrame (pandas.DataFrame): The data you want to process.
        """
        self.dataFrame = dataFrame
        self.results = self.response(warning=dict())
        self.df_results_cleansing()

    @staticmethod
    def contain(string_data: str, compare_data: Union[str, list]) -> dict:
        """
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
        warning_data = dict()
        if string_data in compare_data:
            valid = 1
        else:
            invalid = 1
            warning_data = {
                "message": "Invalid Contain String",
                "value": string_data,
                "detail_message": (f"{string_data} not in list"),
            }
        return valid, invalid, warning_data

    @staticmethod
    def not_contain(string_data: str, compare_data: Union[str, list]) -> dict:
        """
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
        warning_data = dict()
        if string_data not in compare_data:
            valid = 1
        else:
            invalid = 1
            warning_data = {
                "message": "Invalid Not Contain String",
                "value": string_data,
                "detail_message": (f"{string_data} in list"),
            }
        return valid, invalid, warning_data

    @staticmethod
    def regex_contain(regex_data: str, compare_data: Union[str, list]) -> dict:
        """
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
        warning_data = dict()
        regexp = re.compile(r"{}".format(regex_data))
        if regexp.search(compare_data):
            valid = 1
        else:
            invalid = 1
            warning_data = {
                "message": "Invalid regex contain",
                "value": regex_data,
                "detail_message": (f"{regex_data} not in list"),
            }

        return valid, invalid, warning_data

    @staticmethod
    def special_char_contain(
        char: str, compare_data: Union[str, list]
    ) -> dict:
        """
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
        warning_data = dict()
        special_characters = re.compile("[{}]".format(string.punctuation))
        if char in special_characters:
            if char in compare_data:
                valid = 1
            else:
                invalid = 1
            warning_data = {
                "message": "Invalid special character",
                "value": char,
                "detail_message": (f"{char} not in list"),
            }
        else:
            invalid = 1
            warning_data = {
                "message": "your parameter is not special character",
                "value": char,
                "detail_message": (f"{char} not special character"),
            }

        return valid, invalid, warning_data

    def df_is_dataframe(self) -> bool:
        """
        check is param in __init__ is pandas dataframe or not
        :param:
        :return: boolean True or False
        """
        return isinstance(self.dataFrame, pandas.DataFrame)

    def df_is_empty_dataframe(self) -> bool:
        """
        check is an empty dataframe or not

        Args:

        Return:
            boolean True or False
        """
        return self.dataFrame.empty

    def df_contains_empty_value(self) -> dict:
        """
        check is any empty cells or NaN value

        Args:

        Return: row that contains empty cell
        """

        if self.is_dataframe() is True:
            nan_columns = self.dataFrame.columns[
                self.dataFrame.isna().any()
            ].to_list()
            for n in self.dataFrame.columns[
                self.dataFrame.eq("").any()
            ].to_list():
                nan_columns.append(n)

            nan_rows = self.dataFrame[
                self.dataFrame.isnull().any(axis=1)
            ].index.to_list()
            for n in self.dataFrame[
                self.dataFrame.eq("").any(axis=1)
            ].index.to_list():
                nan_rows.append(n)

            if nan_columns != [] or nan_rows != []:
                name = "class_string_df_contains_empty_value"
                warning = {
                    "WARNING": "there are column or row that contain NaN"
                    " or empty string",
                    "value": {
                        "column_nan": nan_columns,
                        "row_nan": nan_rows,
                    },
                }
                self.results["warning"][name] = warning
        else:
            name = "class_string_df_not_dataframe"
            warning = {"WARNING": "This is not dataframe"}
            self.results["warning"][name] = warning

        return self.results

    def df_check_datatype(self, column_name: str = None):
        """
        check all data type in dataframe column

        Args:
            datatype_compare: data type that you want to compare

        Return:
            data type of row or column in dataframe
        """

        if column_name is None:
            list_dtypes = []
            for d in self.dataFrame.dtypes:
                list_dtypes.append(str(d))
            return list_dtypes
        else:
            return str(self.dataFrame[column_name].dtypes)

    def df_results_cleansing(self) -> dict:
        """
        return score cleansing parameter input dataframe

        Args:

        Return:
            dict warning of dataframe cleansing
        """

        # check is dataframe first
        if self.df_is_dataframe() is False:
            name = "class_string_df_not_dataframe"
            warning = {"WARNING": "This is not dataframe"}
            self.results[name] = warning

        # check is empty dataframe
        if self.df_is_empty_dataframe() is True:
            name = "class_string_df_empty_dataframe"
            warning = {"WARNING": "This is not dataframe"}
            self.results[name] = warning

        # check that is contain NaN or empty string
        self.df_contains_empty_value()

        # check and give warning for object data type
        if "object" in self.df_check_datatype():
            name = "class_string_df_check_datatype"
            warning = {
                "WARNING": "contain object datatype, potentially ambiguous"
            }
            self.results["warning"][name] = warning

        return self.results

    def df_contain(self, str_contain) -> dict:
        """
        data quality for string contain.

        Args:
            str_contain: string that want to check

        Return:
            results format
        """

        self.dataFrame["df_contain"] = self.dataFrame.apply(
            lambda row: self.contain(str_contain, row.tolist()), axis=1
        )

        # get score from column
        df_score = pandas.DataFrame(
            self.dataFrame["df_contain"].tolist(), index=self.dataFrame.index
        )
        print(df_score.head())
        valid = sum(df_score[0].to_list())
        invalid = sum(df_score[1].to_list())

        # append warning
        if {} not in df_score[2].to_list():
            warning_data = {
                "message": "Invalid Contain String",
                "value": str_contain,
                "detail_message": (f"{str_contain} not in list"),
            }
            self.results["warning"]["df_contain"] = warning_data

        self.results = self.response(valid, invalid, self.results["warning"])

        return self.results

    def df_column_contain(self, str_contain, column_name) -> dict:
        """
        data quality for string contain.

        Args:
            str_contain: string that want to check
            column_name: column name that want to check

        Return:
            results format
        """
        valid = 0
        invalid = 0
        warning = dict()

        for index, str_data in enumerate(self.dataFrame[column_name]):
            try:
                if isinstance(str_data, (str)) is False:
                    raise InvalidDataTypeWarning(warning)
                valid_row, invalid_row, warning_data = self.contain(
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
                warning_data = {
                    "message": "Invalid Data Type",
                    "value": str_data,
                    "detail_message": "Value must be of string data type",
                }
                warning[index] = InvalidDataTypeWarning(warning_data).message
        result = self.response(valid, invalid, warning)
        return result

    def df_not_contain(self, str_not_contain) -> dict:
        """
        data quality for string not contain.

        Args:
            str_not_contain: string that want to check

        Return:
            results format
        """
        return self.results

    def df_column_not_contain(self, str_not_contain, column):
        """
        data quality for string not contain.
        if you don't put is_check_column, the script will check
        through dataframe and return row index
        :param is_check_column: if you want to check column only
        :param str_not_contain: string that want to check
        return: results format
        """

        valid = 0
        invalid = 0
        warning = dict()

        for index, str_data in enumerate(self.dataFrame[column]):
            try:
                if isinstance(str_data, (str)) is False:
                    raise InvalidDataTypeWarning(warning)
                valid_row, invalid_row, warning_data = self.not_contain(
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
                warning_data = {
                    "message": "Invalid Data Type",
                    "value": str_data,
                    "detail_message": "Value must be of string data type",
                }
                warning[index] = InvalidDataTypeWarning(warning_data).message
        result = self.response(valid, invalid, warning)
        return result

    def df_regex_contain(self, regex_data) -> dict:
        """
        data quality for regex not contain.

        Args:
            regex_data: regex string that want to check

        Return:
            results format
        """
        self.dataFrame["df_regex_contain"] = self.dataFrame.apply(
            lambda row: self.regex_contain(regex_data, row.tolist()), axis=1
        )

        # get score from column
        df_score = pandas.DataFrame(
            self.dataFrame["df_regex_contain"].tolist(),
            index=self.dataFrame.index,
        )
        print(df_score.head())
        valid = sum(df_score[0].to_list())
        invalid = sum(df_score[1].to_list())

        # append warning
        if {} not in df_score[2].to_list():
            warning_data = {
                "message": "Invalid Regex Contain",
                "value": regex_data,
                "detail_message": (f"{regex_data} not in regex contain list"),
            }
            self.results["warning"]["df_regex_contain"] = warning_data

        self.results = self.response(valid, invalid, self.results["warning"])

        return self.results

    def df_column_regex_contain(self, regex_data, column_name) -> dict:
        """
        data quality for regex not contain.

        Args:
            regex_data: regex string that want to check
            column_name: column name that want to check

        Return:
            results format
        """
        valid = 0
        invalid = 0
        warning = dict()

        for index, str_data in enumerate(self.dataFrame[column_name]):
            try:
                if isinstance(str_data, (str)) is False:
                    raise InvalidDataTypeWarning(warning)
                valid_row, invalid_row, warning_data = self.contain(
                    regex_data, str_data
                )
                valid += valid_row
                invalid += invalid_row
                if warning_data != {}:
                    warning[index] = InvalidDataValueWarning(
                        warning_data
                    ).message
            except InvalidDataTypeWarning:
                invalid += 1
                warning_data = {
                    "message": "Invalid Data Type",
                    "value": str_data,
                    "detail_message": "Value must be of string data type",
                }
                warning[index] = InvalidDataTypeWarning(warning_data).message
        result = self.response(valid, invalid, warning)
        return result

    def df_special_char_contain(self, char) -> dict:
        """
        data quality for special char contain.

        Args:
            char: char string that want to check

        Return:
            results format
        """
        self.dataFrame["df_special_char_contain"] = self.dataFrame.apply(
            lambda row: self.special_char_contain(char, row.tolist()), axis=1
        )

        # get score from column
        df_score = pandas.DataFrame(
            self.dataFrame["df_special_char_contain"].tolist(),
            index=self.dataFrame.index,
        )
        print(df_score.head())
        valid = sum(df_score[0].to_list())
        invalid = sum(df_score[1].to_list())

        # append warning
        if {} not in df_score[2].to_list():
            warning_data = {
                "message": "Invalid Special char Contain",
                "value": char,
                "detail_message": (f"{char} not in contain list"),
            }
            self.results["warning"]["df_special_char_contain"] = warning_data

        self.results = self.response(valid, invalid, self.results["warning"])

        return self.results

    def df_column_special_char_contain(self, char, column_name) -> dict:
        """
        data quality for special char contain.

        Args:
            char: char string that want to check
            column_name: column name that want to check

        Return:
            results format
        """
        valid = 0
        invalid = 0
        warning = dict()

        for index, str_data in enumerate(self.dataFrame[column_name]):
            try:
                if isinstance(str_data, (str)) is False:
                    raise InvalidDataTypeWarning(warning)
                (
                    valid_row,
                    invalid_row,
                    warning_data,
                ) = self.special_char_contain(char, str_data)
                valid += valid_row
                invalid += invalid_row
                if warning_data != {}:
                    warning[index] = InvalidDataValueWarning(
                        warning_data
                    ).message
            except InvalidDataTypeWarning:
                invalid += 1
                warning_data = {
                    "message": "Invalid Data Type",
                    "value": str_data,
                    "detail_message": "Value must be of string data type",
                }
                warning[index] = InvalidDataTypeWarning(warning_data).message
        result = self.response(valid, invalid, warning)
        return result

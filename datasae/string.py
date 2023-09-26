#!/usr/bin/env python3

# This module is part of DataSae and is released under
# the AGPL-3.0-only License: https://opensource.org/license/agpl-v3/


from exception import (
    InvalidDataTypeWarning,
    InvalidDataValueWarning,
    EmptyDataFrame,
)
from utils import Basic, create_warning_data, WarningDataMessage
from typing import Union
import pandas as pd
import re


class WarningDataDetailMessage:
    STRING_DATA_TYPE: str = "Value must be of string data type"


class String(Basic):
    def __init__(self, dataFrame: pd.DataFrame):
        """
        Initializes an instance of the String class.

        Args:
            dataFrame (pd.DataFrame): The data you want to process.
        """
        self.dataFrame = dataFrame
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
        warning_data = {}
        if string_data in compare_data:
            valid = 1
        else:
            invalid = 1
            warning_data = create_warning_data(
                compare_data, f"Value should be contain to {string_data}"
            )
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
        warning_data = {}
        if string_data not in compare_data:
            valid = 1
        else:
            invalid = 1
            warning_data = create_warning_data(
                compare_data, f"Value should be not contain to {string_data}"
            )
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
        warning_data = {}
        regexp = re.compile(r"{}".format(regex_data))
        if regexp.search(compare_data):
            valid = 1
        else:
            invalid = 1
            warning_data = create_warning_data(
                compare_data, f"Value should be regex contain to {regex_data}"
            )

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
        warning_data = {}
        punctuation = """[!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"""
        if char in punctuation:
            if char in compare_data:
                valid = 1
            else:
                invalid = 1
                warning_data = create_warning_data(
                    compare_data, f"Value should be contain to {char}"
                )
        else:
            invalid = 1
            warning_data = create_warning_data(
                compare_data,
                f"Value is not special character compare to {char}",
            )

        return valid, invalid, warning_data

    @staticmethod
    def length(str_data: str) -> int:
        """
        Check if given character length

        Args:
            char (str): The string char value to be checked.

        Returns:
            int: an integer of char length.
        """

        return len(str_data)

    @staticmethod
    def word_count(str_data: str) -> int:
        """
        Check if given character word count

        Args:
            char (str): The string char value to be checked.

        Returns:
            int: an integer of char length.
        """

        # remove all special char
        str_data = "".join(
            letter
            for letter in str_data
            if letter.isalnum() or letter == " " or letter == "\n"
        )
        # count by space
        return len(str_data.split())

    @staticmethod
    def is_uppercase(str_data: str) -> dict:
        """
        Check if given character is all uppercase or not

        Args:
            str_data (str): The string char value to be checked.

        Returns:
            dict: a dict type of result
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
    def is_lowercase(str_data: str) -> bool:
        """
        Check if given character is all lower case or not

        Args:
            str_data (str): The string char value to be checked.

        Returns:
            bool: a boolean True or False
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
    def is_capitalize_first_word(str_data: str) -> bool:
        """
        Check if given character is capitalize in first word

        Args:
            str_data (str): The string char value to be checked.

        Returns:
            bool: a boolean True or False
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
    def is_capitalize_all_word(str_data: str) -> bool:
        """
        Check if given character is capitalize in all word

        Args:
            str_data (str): The string char value to be checked.

        Returns:
            bool: a boolean True or False
        """

        valid = 0
        invalid = 0
        warning_data = {}
        if str_data.title():
            valid = 1
        else:
            invalid = 1
            warning_data = create_warning_data(
                str_data, "Value should capitalize all word"
            )

        return valid, invalid, warning_data

    def df_is_dataframe(self) -> bool:
        """
        check is param in __init__ is pandas dataframe or not
        :param:
        :return: boolean True or False
        """
        if self.dataFrame is not None:
            return isinstance(self.dataFrame, pd.DataFrame)
        else:
            return False

    def df_is_empty_dataframe(self) -> bool:
        """
        check is an empty dataframe or not

        Args:

        Return:
            boolean True or False
        """
        if self.df_is_dataframe():
            return self.dataFrame.empty

    def df_contains_empty_value(self) -> dict:
        """
        check is any empty cells or NaN value

        Args:

        Return: row that contains empty cell
        """
        warning = {}

        if self.df_is_dataframe() and self.df_is_empty_dataframe() is False:
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
                warning = create_warning_data(
                    name, "value contain empty or NaN"
                )
        else:
            name = "class_string_df_not_dataframe"
            warning = create_warning_data(name, "value is not a dataframe")

        return warning

    def df_check_datatype(self, column_name: str = None) -> dict:
        """
        check all data type in dataframe column

        Args:
            column_name: column name of dataframe

        Return:
            data type of row or column in dataframe
        """

        valid = 0
        invalid = 0
        warning = {}
        if self.df_is_dataframe():
            # only receive string datatype
            if column_name is None:
                columns = self.dataFrame.columns.to_list()
            else:
                columns = [column_name]

            for c in columns:
                loop = 0
                for cell in self.dataFrame[c].apply(type).to_list():
                    if cell.__name__ != 'str':
                        invalid += 1
                        warning = create_warning_data(
                            self.dataFrame[c],
                            WarningDataDetailMessage.STRING_DATA_TYPE,
                            WarningDataMessage.INVALID_DATA_TYPE,
                        )
                    loop += 1

        return valid, invalid, warning

    def df_results_cleansing(self) -> dict:
        """
        return score cleansing parameter input dataframe

        Args:

        Return:
            dict warning of dataframe cleansing
        """
        valid = 0
        invalid = 0
        warning = {}

        if self.dataFrame is not None:
            # check is dataframe first
            if self.df_is_dataframe() is False:
                name = "class_string_df_not_dataframe"
                warning = create_warning_data(name, "value not a dataframe")
                invalid = 1
                result = self.response(valid, invalid, warning)
                return result

            # check is empty dataframe
            if self.df_is_empty_dataframe() is True:
                name = "class_string_df_empty_dataframe"
                warning = create_warning_data(name, EmptyDataFrame().message)
                invalid = 1
                result = self.response(valid, invalid, warning)
                return result

            # check that is contain NaN or empty string
            warning = self.df_contains_empty_value()
        else:
            name = "class_string_none"
            warning = create_warning_data(name, EmptyDataFrame().message)
            invalid = 1
            result = self.response(valid, invalid, warning)
            return result

        result = self.response(valid, invalid, warning)
        return result

    def df_contain(self, str_contain) -> dict:
        """
        data quality for string contain.

        Args:
            str_contain: string that want to check

        Return:
            results format
        """
        valid = 0
        invalid = 0
        warning = {}

        # cleansing first
        df_results_cleansing = self.df_results_cleansing()
        if df_results_cleansing["invalid"] == 1:
            return df_results_cleansing
        elif df_results_cleansing["warning"] != {}:
            warning["df_results_cleansing"] = df_results_cleansing["warning"]

        if self.df_is_dataframe():
            try:
                if isinstance(str_contain, (str)) is False:
                    raise InvalidDataTypeWarning(warning)
            except InvalidDataTypeWarning:
                invalid += 1
                warning_data = create_warning_data(
                    str_contain,
                    WarningDataDetailMessage.STRING_DATA_TYPE,
                    WarningDataMessage.INVALID_DATA_TYPE,
                )
                warning[0] = InvalidDataTypeWarning(warning_data).message

            self.dataFrame["df_contain"] = self.dataFrame.apply(
                lambda row: self.contain(str_contain, row.tolist()), axis=1
            )

            # get score from column
            df_score = pd.DataFrame(
                self.dataFrame["df_contain"].tolist(),
                index=self.dataFrame.index,
            )
            valid = sum(df_score[0].to_list())
            invalid = sum(df_score[1].to_list())

            index = 0
            for w in df_score[2].to_list():
                warning[index] = w
                index += 1

            results = self.response(valid, invalid, warning)

            return results

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
        warning = {}

        # cleansing first
        df_results_cleansing = self.df_results_cleansing()
        if df_results_cleansing["invalid"] == 1:
            return df_results_cleansing
        elif df_results_cleansing["warning"] != {}:
            warning["df_results_cleansing"] = df_results_cleansing["warning"]

        if self.df_is_dataframe():
            try:
                if isinstance(str_contain, (str)) is False:
                    raise InvalidDataTypeWarning(warning)
            except InvalidDataTypeWarning:
                invalid += 1
                warning_data = create_warning_data(
                    str_contain,
                    WarningDataDetailMessage.STRING_DATA_TYPE,
                    WarningDataMessage.INVALID_DATA_TYPE,
                )
                warning["str_contain"] = InvalidDataTypeWarning(
                    warning_data
                ).message

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
                    warning_data = create_warning_data(
                        str_data,
                        WarningDataDetailMessage.STRING_DATA_TYPE,
                        WarningDataMessage.INVALID_DATA_TYPE,
                    )
                    warning[index] = InvalidDataTypeWarning(
                        warning_data
                    ).message
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

        valid = 0
        invalid = 0
        warning = {}

        # cleansing first
        df_results_cleansing = self.df_results_cleansing()
        if df_results_cleansing["invalid"] == 1:
            return df_results_cleansing
        elif df_results_cleansing["warning"] != {}:
            warning["df_results_cleansing"] = df_results_cleansing["warning"]

        if self.df_is_dataframe():
            try:
                if isinstance(str_not_contain, (str)) is False:
                    raise InvalidDataTypeWarning(warning)
            except InvalidDataTypeWarning:
                invalid += 1
                warning_data = create_warning_data(
                    str_not_contain,
                    WarningDataDetailMessage.STRING_DATA_TYPE,
                    WarningDataMessage.INVALID_DATA_TYPE,
                )
                warning["df_not_contain"] = InvalidDataTypeWarning(
                    warning_data
                ).message

            self.dataFrame["df_contain"] = self.dataFrame.apply(
                lambda row: self.not_contain(str_not_contain, row.tolist()),
                axis=1,
            )

            # get score from column
            df_score = pd.DataFrame(
                self.dataFrame["df_not_contain"].tolist(),
                index=self.dataFrame.index,
            )
            valid = sum(df_score[0].to_list())
            invalid = sum(df_score[1].to_list())

            index = 0
            for w in df_score[2].to_list():
                warning[index] = w
                index += 1

            results = self.response(valid, invalid, warning)

            return results

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
        warning = {}

        # cleansing first
        df_results_cleansing = self.df_results_cleansing()
        if df_results_cleansing["invalid"] == 1:
            return df_results_cleansing
        elif df_results_cleansing["warning"] != {}:
            warning["df_results_cleansing"] = df_results_cleansing["warning"]

        if self.df_is_dataframe():
            try:
                if isinstance(str_not_contain, (str)) is False:
                    raise InvalidDataTypeWarning(warning)
            except InvalidDataTypeWarning:
                invalid += 1
                warning_data = create_warning_data(
                    str_not_contain,
                    WarningDataDetailMessage.STRING_DATA_TYPE,
                    WarningDataMessage.INVALID_DATA_TYPE,
                )
                warning["df_not_contain"] = InvalidDataTypeWarning(
                    warning_data
                ).message

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
                    warning_data = warning_data = create_warning_data(
                        str_data,
                        WarningDataDetailMessage.STRING_DATA_TYPE,
                        WarningDataMessage.INVALID_DATA_TYPE,
                    )
                    warning[index] = InvalidDataTypeWarning(
                        warning_data
                    ).message
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
        valid = 0
        invalid = 0
        warning = {}

        # cleansing first
        df_results_cleansing = self.df_results_cleansing()
        if df_results_cleansing["invalid"] == 1:
            return df_results_cleansing
        elif df_results_cleansing["warning"] != {}:
            warning["df_results_cleansing"] = df_results_cleansing["warning"]

        if self.df_is_dataframe():
            try:
                if isinstance(regex_data, (str)) is False:
                    raise InvalidDataTypeWarning(warning)
            except InvalidDataTypeWarning:
                invalid += 1
                warning_data = create_warning_data(
                    regex_data,
                    WarningDataDetailMessage.STRING_DATA_TYPE,
                    WarningDataMessage.INVALID_DATA_TYPE,
                )
                warning["df_regex_contain"] = InvalidDataTypeWarning(
                    warning_data
                ).message
            self.dataFrame["df_regex_contain"] = self.dataFrame.apply(
                lambda row: self.regex_contain(regex_data, row.tolist()),
                axis=1,
            )

            # get score from column
            df_score = pd.DataFrame(
                self.dataFrame["df_regex_contain"].tolist(),
                index=self.dataFrame.index,
            )
            valid = sum(df_score[0].to_list())
            invalid = sum(df_score[1].to_list())

            index = 0
            for w in df_score[2].to_list():
                warning[index] = w
                index += 1

            results = self.response(valid, invalid, warning)

            return results

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
        warning = {}

        # cleansing first
        df_results_cleansing = self.df_results_cleansing()
        if df_results_cleansing["invalid"] == 1:
            return df_results_cleansing
        elif df_results_cleansing["warning"] != {}:
            warning["df_results_cleansing"] = df_results_cleansing["warning"]

        if self.df_is_dataframe():
            try:
                if isinstance(regex_data, (str)) is False:
                    raise InvalidDataTypeWarning(warning)
            except InvalidDataTypeWarning:
                invalid += 1
                warning_data = create_warning_data(
                    regex_data,
                    WarningDataDetailMessage.STRING_DATA_TYPE,
                    WarningDataMessage.INVALID_DATA_TYPE,
                )
                warning["df_not_contain"] = InvalidDataTypeWarning(
                    warning_data
                ).message

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
                    warning_data = create_warning_data(
                        str_data,
                        WarningDataDetailMessage.STRING_DATA_TYPE,
                        WarningDataMessage.INVALID_DATA_TYPE,
                    )
                    warning[index] = InvalidDataTypeWarning(
                        warning_data
                    ).message
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
        valid = 0
        invalid = 0
        warning = {}

        # cleansing first
        df_results_cleansing = self.df_results_cleansing()
        if df_results_cleansing["invalid"] == 1:
            return df_results_cleansing
        elif df_results_cleansing["warning"] != {}:
            warning["df_results_cleansing"] = df_results_cleansing["warning"]

        if self.df_is_dataframe():
            try:
                if isinstance(char, (str)) is False:
                    raise InvalidDataTypeWarning(warning)
            except InvalidDataTypeWarning:
                invalid += 1
                warning_data = create_warning_data(
                    char,
                    WarningDataDetailMessage.STRING_DATA_TYPE,
                    WarningDataMessage.INVALID_DATA_TYPE,
                )
                warning["df_not_contain"] = InvalidDataTypeWarning(
                    warning_data
                ).message
            self.dataFrame["df_special_char_contain"] = self.dataFrame.apply(
                lambda row: self.special_char_contain(char, row.tolist()),
                axis=1,
            )

            # get score from column
            df_score = pd.DataFrame(
                self.dataFrame["df_special_char_contain"].tolist(),
                index=self.dataFrame.index,
            )

            valid = sum(df_score[0].to_list())
            invalid = sum(df_score[1].to_list())

            index = 0
            for w in df_score[2].to_list():
                warning[index] = w
                index += 1

            self.results = self.response(valid, invalid, warning)

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
        warning = {}

        # cleansing first
        df_results_cleansing = self.df_results_cleansing()
        if df_results_cleansing["invalid"] == 1:
            return df_results_cleansing
        elif df_results_cleansing["warning"] != {}:
            warning["df_results_cleansing"] = df_results_cleansing["warning"]

        if self.df_is_dataframe():
            try:
                if isinstance(char, (str)) is False:
                    raise InvalidDataTypeWarning(warning)
            except InvalidDataTypeWarning:
                invalid += 1
                warning_data = create_warning_data(
                    char,
                    WarningDataDetailMessage.STRING_DATA_TYPE,
                    WarningDataMessage.INVALID_DATA_TYPE,
                )
                warning["df_not_contain"] = InvalidDataTypeWarning(
                    warning_data
                ).message

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
                    warning_data = create_warning_data(
                        str_data,
                        WarningDataDetailMessage.STRING_DATA_TYPE,
                        WarningDataMessage.INVALID_DATA_TYPE,
                    )
                    warning[index] = InvalidDataTypeWarning(
                        warning_data
                    ).message
            result = self.response(valid, invalid, warning)
            return result

    def df_column_length(self, column_name) -> pd.DataFrame:
        """
        data quality for length of string.

        Args:
            column_name: column name of df that want to check

        Return:
            dataframe results format
        """
        if self.df_is_dataframe():
            self.dataFrame[
                "df_length_{}".format(column_name)
            ] = self.dataFrame.apply(
                lambda row: self.length(row[column_name]), axis=1
            )

            return self.dataFrame

    def df_column_word_count(self, column_name) -> pd.DataFrame:
        """
        data quality for word count of string

        Args:
            column_name: column name of df that want to check

        Return:
            dataframe results format
        """

        if self.df_is_dataframe():
            self.dataFrame[
                "df_word_count_{}".format(column_name)
            ] = self.dataFrame.apply(
                lambda row: self.word_count(row[column_name]), axis=1
            )

            return self.dataFrame

    def df_column_is_uppercase(self, column_name) -> dict:
        """
        data quality for check in column is uppercase

        Args:
            column_name: column name of df that want to check

        Return:
            dataframe results format
        """
        valid = 0
        invalid = 0
        warning = {}

        # cleansing first
        df_results_cleansing = self.df_results_cleansing()
        if df_results_cleansing["invalid"] == 1:
            return df_results_cleansing
        elif df_results_cleansing["warning"] != {}:
            warning["df_results_cleansing"] = df_results_cleansing["warning"]

        if self.df_is_dataframe():
            self.dataFrame[
                "df_is_uppercase_{}".format(column_name)
            ] = self.dataFrame.apply(
                lambda row: self.is_uppercase(row[column_name]), axis=1
            )

            # get score from column
            df_score = pd.DataFrame(
                self.dataFrame[
                    "df_is_uppercase_{}".format(column_name)
                ].tolist(),
                index=self.dataFrame.index,
            )

            valid = sum(df_score[0].to_list())
            invalid = sum(df_score[1].to_list())

            index = 0
            for w in df_score[2].to_list():
                warning[index] = w
                index += 1

            results = self.response(valid, invalid, warning)

            return results

    def df_column_is_lowercase(self, column_name) -> dict:
        """
        data quality for check in column is lower case

        Args:
            column_name: column name of df that want to check

        Return:
            dataframe results format
        """
        valid = 0
        invalid = 0
        warning = {}

        # cleansing first
        df_results_cleansing = self.df_results_cleansing()
        if df_results_cleansing["invalid"] == 1:
            return df_results_cleansing
        elif df_results_cleansing["warning"] != {}:
            warning["df_results_cleansing"] = df_results_cleansing["warning"]

        if self.df_is_dataframe():
            self.dataFrame[
                "df_is_lowercase_{}".format(column_name)
            ] = self.dataFrame.apply(
                lambda row: self.is_lowercase(row[column_name]), axis=1
            )

            # get score from column
            df_score = pd.DataFrame(
                self.dataFrame[
                    "df_is_lowercase_{}".format(column_name)
                ].tolist(),
                index=self.dataFrame.index,
            )

            valid = sum(df_score[0].to_list())
            invalid = sum(df_score[1].to_list())

            index = 0
            for w in df_score[2].to_list():
                warning[index] = w
                index += 1

            results = self.response(valid, invalid, warning)

            return results

    def df_column_is_capitalize_first_word(self, column_name) -> dict:
        """
        data quality for check in column is capitalize in first word

        Args:
            column_name: column name of df that want to check

        Return:
            dataframe results format
        """
        valid = 0
        invalid = 0
        warning = {}

        # cleansing first
        df_results_cleansing = self.df_results_cleansing()
        if df_results_cleansing["invalid"] == 1:
            return df_results_cleansing
        elif df_results_cleansing["warning"] != {}:
            warning["df_results_cleansing"] = df_results_cleansing["warning"]

        if self.df_is_dataframe():
            self.dataFrame[
                "df_is_capitalize_first_word_{}".format(column_name)
            ] = self.dataFrame.apply(
                lambda row: self.is_capitalize_first_word(row[column_name]),
                axis=1,
            )

            # get score from column
            df_score = pd.DataFrame(
                self.dataFrame[
                    "df_is_capitalize_first_word_{}".format(column_name)
                ].tolist(),
                index=self.dataFrame.index,
            )

            valid = sum(df_score[0].to_list())
            invalid = sum(df_score[1].to_list())

            index = 0
            for w in df_score[2].to_list():
                warning[index] = w
                index += 1

            results = self.response(valid, invalid, warning)

            return results

    def df_column_is_capitalize_all_word(self, column_name) -> dict:
        """
        data quality for check in column is capitalize in all word

        Args:
            column_name: column name of df that want to check

        Return:
            dataframe results format
        """
        valid = 0
        invalid = 0
        warning = {}

        # cleansing first
        df_results_cleansing = self.df_results_cleansing()
        if df_results_cleansing["invalid"] == 1:
            return df_results_cleansing
        elif df_results_cleansing["warning"] != {}:
            warning["df_results_cleansing"] = df_results_cleansing["warning"]

        if self.df_is_dataframe():
            self.dataFrame[
                "df_is_capitalize_all_word_{}".format(column_name)
            ] = self.dataFrame.apply(
                lambda row: self.is_capitalize_all_word(row[column_name]),
                axis=1,
            )

            # get score from column
            df_score = pd.DataFrame(
                self.dataFrame[
                    "df_is_capitalize_all_word_{}".format(column_name)
                ].tolist(),
                index=self.dataFrame.index,
            )

            valid = sum(df_score[0].to_list())
            invalid = sum(df_score[1].to_list())

            index = 0
            for w in df_score[2].to_list():
                warning[index] = w
                index += 1

            results = self.response(valid, invalid, warning)

            return results

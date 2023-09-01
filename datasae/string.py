#!/usr/bin/env python3

# This module is part of DataSae and is released under
# the AGPL-3.0-only License: https://opensource.org/license/agpl-v3/

import pandas


class String:
    """Checking Data Quality of pandas dataframe with string data type"""

    def __init__(self, df: pandas.DataFrame):
        """
        Initialize dataframe that is wanted to check.
        :param df: dataframe that is wanted to check.
        """
        self.df = df
        self.results = self.results_format()

    def results_format(self):
        """
        globalize default data quality checking results format
        :param:
        :return: dict of default data quality result
        """

        return {
            "name": None,
            "score": None,
            "df_row_index": [],
            "df_column_names": [],
            "message": [],
        }

    def is_dataframe(self):
        """
        check is param in __init__ is pandas dataframe or not
        :param:
        :return: boolean True or False
        """
        return isinstance(self.df, pandas.DataFrame)

    def is_empty_dataframe(self):
        """
        check is an empty dataframe or not
        :param:
        :return: boolean True or False
        """
        return self.df.empty

    def df_contains_empty_value(self):
        """
        check is any empty cells or NaN value
        :param:
        :return: row that contains empty cell
        """

        nan_columns = self.df.columns[self.df.isna().any()].to_list()
        for n in self.df.columns[self.df.eq("").any()].to_list():
            nan_columns.append(n)

        nan_rows = self.df[self.df.isnull().any(axis=1)].index.to_list()
        for n in self.df[self.df.eq("").any(axis=1)].index.to_list():
            nan_rows.append(n)

        if nan_columns != [] or nan_rows != []:
            self.results["message"].append(
                {
                    "WARNING": "there are column or row that contain NaN"
                    " or empty string",
                    "value": {"column_nan": nan_columns, "row_nan": nan_rows},
                }
            )

        return self.results

    def results_df_cleansing(self):
        """
        return score cleansing parameter input dataframe
        :param:
        return: score of dataframe cleansing
        """

        # check is dataframe first
        if self.is_dataframe() is False:
            self.results["score"] = 0
            self.results["message"].append(
                {"ERROR": "parameter input is not a dataframe"}
            )

        # check is empty dataframe
        if self.is_empty_dataframe() is True:
            self.results["score"] = 0
            self.results["message"].append(
                {"ERROR": "parameter input is an empty dataframe"}
            )

        # check that is contain NaN or empty string
        self.df_contains_empty_value()

        return self.results

    def df_contain(self, str_contain, is_check_column: bool = None):
        """
        data quality for string contain.
        if you don't put is_check_column, the script will check
        through dataframe and return row index
        :param is_check_column: if you want to check column only
        :param str_contain: string that want to check
        return: results format
        """

        # any data quality checking should check this standard cleansing
        self.results_df_cleansing()

        key = None
        if is_check_column is None:
            if is_check_column is not True:
                result_df = self.df[
                    self.df.eq(str_contain).any(axis=1)
                ].index.to_list()
                key = "df_row_index"

        if key is None:
            result_df = self.df.columns[
                self.df.eq(str_contain).any()
            ].to_list()
            key = "df_column_names"

        for r in result_df:
            self.results[key].append(r)

        self.results["name"] = "string_contain"
        return self.results

    def df_not_contain(self, str_not_contain, is_check_column: bool = None):
        """
        data quality for string not contain.
        if you don't put is_check_column, the script will check
        through dataframe and return row index
        :param is_check_column: if you want to check column only
        :param str_not_contain: string that want to check
        return: results format
        """

        # any data quality checking should check this standard cleansing
        self.results_df_cleansing()

        key = None
        if is_check_column is None:
            if is_check_column is not True:
                result_df = self.df[
                    ~self.df.eq(str_not_contain).any(axis=1)
                ].index.to_list()
                key = "df_row_index"

        if key is None:
            result_df = self.df.columns[
                ~self.df.eq(str_not_contain).any()
            ].to_list()
            key = "df_column_names"

        for r in result_df:
            self.results[key].append(r)

        self.results["name"] = "string_not_contain"
        return self.results

    def is_df_contain(self, str_contain, is_check_column: bool = None):
        """
        data quality for string contain.
        if you don't put is_check_column, the script will check
        through dataframe and return row index
        :param is_check_column: if you want to check column only
        :param str_contain: string that want to check
        return: boolean
        """

        self.df_contain(str_contain, is_check_column)
        if (
            self.results["df_row_index"] != []
            and self.results["df_column_names"] != []
        ):
            return True
        else:
            return False

    def is_df_not_contain(self, str_not_contain, is_check_column: bool = None):
        """
        data quality for string not contain.
        if you don't put is_check_column, the script will check
        through dataframe and return row index
        :param is_check_column: if you want to check column only
        :param str_contain: string that want to check
        return: boolean
        """

        self.df_not_contain(str_not_contain, is_check_column)
        # if row result same as row df
        # or if column name same as column df
        if (
            self.results["df_row_index"] == self.df.index.to_list()
            or self.results["df_column_names"] == self.df.columns.to_list()
        ):
            return True
        else:
            return False

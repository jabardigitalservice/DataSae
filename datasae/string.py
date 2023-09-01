#!/usr/bin/env python3

# This module is part of DataSae and is released under
# the AGPL-3.0-only License: https://opensource.org/license/agpl-v3/

import pandas


class String():
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

        return {'score': 0,
                'message': []}

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
        for n in self.df.columns[self.df.eq('').any()].to_list():
            nan_columns.append(n)

        nan_rows = self.df[self.df.isnull().any(axis=1)].index.to_list()
        for n in self.df[self.df.eq('').any(axis=1)].index.to_list():
            nan_rows.append(n)

        if nan_columns != [] or nan_rows != []:
            self.results['message'].append({
                'WARNING': 'there are column and row that contain NaN'
                           'or empty string',
                'value': {'column_nan': nan_columns,
                          'row_nan': nan_rows}
            })

        return self.results

    def results_df_cleansing(self):
        """
        return score cleansing parameter dataframe
        :param:
        return: score of dataframe cleansing
        """

        # check is dataframe first
        if self.is_dataframe() is False:
            self.results['score'] = 0
            self.results['message'].append(
                {'ERROR': 'parameter input is not a dataframe'}
            )

        return self.results

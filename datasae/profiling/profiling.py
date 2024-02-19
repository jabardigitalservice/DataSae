#!/usr/bin/env python3

# Copyright (C) Free Software Foundation, Inc. All rights reserved.
# Licensed under the AGPL-3.0-only License. See LICENSE in the project root
# for license information.

"""Library data quality for data profling."""

import pandas as pd

from ..utils import Basic
from IPython.display import display


class Profiling(Basic):
    """Data Profiling."""

    def __init__(self, dataFrame: pd.DataFrame):
        """
        Instance initialitzation of the Integer class.

        Args:
            dataFrame (pd.DataFrame): The data you want to process.
        """
        self.dataFrame = dataFrame

    @staticmethod
    def check_number_of_observations(columns: list) -> int:
        """
        Check the number of observations in a given list of columns.

        Args:
            columns (list): A list of columns in a pandas DataFrame.

        Returns:
            int: A integer containing the total number of columns.
        """
        total = len(columns)
        return total

    @staticmethod
    def check_duplicate_rows(df: pd.DataFrame) -> int:
        """
        Check the number of duplicate rows in a given list of columns.

        Args:
            df (pd.DataFrame): A defined pandas DataFrame.

        Returns:
            int: An integer containing the total number of columns.
        """
        total = len(df[df.duplicated(keep=False)])
        return total

    @staticmethod
    def check_head_and_tail(df: pd.DataFrame) -> pd.DataFrame:
        """
        Generate sample of first and last 5 rows of a DataFrame.

        Args:
            df (pd.DataFrame): A defined pandas DataFrame.

        Returns:
            pd.DataFrame: Sample of first and last 5 rows of a DataFrame.
        """
        def get_head_tail(df):
            head = df.head()
            tail = df.tail()
            print("Head: first 5 rows")
            display(head)
            print("Tail: last 5 rows")
            display(tail)

        sample = get_head_tail(df)
        return sample

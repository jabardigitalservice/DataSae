#!/usr/bin/env python3

# Copyright (C) Free Software Foundation, Inc. All rights reserved.
# Licensed under the AGPL-3.0-only License. See LICENSE in the project root
# for license information.

"""Library data quality for data profling."""

import pandas as pd

from ..utils import Basic


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
    def check_duplicate_rows(data: dict) -> int:
        """
        Check the number of duplicate rows in a given list of columns.

        Args:
            data (dict): A dictionary that contains the data.

        Returns:
            int: An integer containing the total number of columns.
        """
        counts = {}
        max_count = 0
        for row in zip(*data.values()):
            counts[row] = counts.get(row, 0) + 1
            max_count = max(max_count, counts[row])

        return max_count if max_count > 1 else 0

    @staticmethod
    def check_head_and_tail(data: dict) -> dict:
        """
        Generate sample of first and last 5 rows of a DataFrame.

        Args:
            data (dict): A dictionary that contains the data.

        Returns:
            dict: A dictionary of first and last 5 rows of a DataFrame.
        """
        head, tail = {}, {}
        for key, value in data.items():
            head[key] = value[:5]
            tail[key] = value[-5:]

        return head, tail

#!/usr/bin/env python3

# Copyright (C) Free Software Foundation, Inc. All rights reserved.
# Licensed under the AGPL-3.0-only License. See LICENSE in the project root
# for license information.

"""Library data quality for data profling."""

import re

import pandas as pd
from collections import defaultdict

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
    def check_number_of_observations(data: list) -> int:
        """
        Check the number of observations in a given list of data.

        Args:
            data (list): A list of data in a pandas DataFrame.

        Returns:
            int: A integer containing the total number of data.
        """
        count = len(data)
        return count

    @staticmethod
    def check_duplicate_rows(data: list) -> int:
        """
        Check the number of duplicate rows in a given list of columns.

        Args:
            data (dict): A dictionary that contains the data.

        Returns:
            int: An integer containing the total number of columns.
        """
        counts = {}
        counts = defaultdict(int)
        for dictionary in data:
            frozen_dict = frozenset(dictionary.items())
            counts[frozen_dict] += 1

        duplicates = {k: v for k, v in counts.items() if v > 1}
        count = len(duplicates)
        return count

    @staticmethod
    def check_head_and_tail(data: list) -> dict:
        """
        Generate sample of first and last 5 rows of a DataFrame.

        Args:
            data (dict): A dictionary that contains the data.

        Returns:
            dict: A dictionary of first and last 5 rows of a DataFrame.
        """
        head, tail = data[:5], data[-5:]

        return head, tail

    @staticmethod
    def check_number_of_variables(columns: list) -> int:
        """
        Generate the number of variables in a given list of columns.

        Args:
            columns (list): A list of columns in a pandas DataFrame.

        Returns:
            int: A integer containing the total number of columns.
        """
        count = len(columns)
        return count

    @staticmethod
    def check_missing_cells(data: list) -> int:
        """
        Check any missing cells of a DataFrame.

        Args:
            data (list): A list of dictionary that contains the data.

        Returns:
            int: An int of total missing cells of a DataFrame.
        """
        missing_cells = 0
        for row in data:
            value = list(row.values())
            value = [
                a.strip() if isinstance(a, str) else a for a in value
            ]
            value = [
                ""
                if (isinstance(a, float) or isinstance(a, int))
                and str(a).lower() == "nan"
                else a
                for a in value
            ]

            missing_cells += len(value.index(None))
            missing_cells += len(value.index(""))

        return missing_cells

    @staticmethod
    def check_characters_and_unicode(data: list) -> dict:
        """
        Check total characters and unicode of a DataFrame.

        Args:
            data (list): A list of dictionary that contains the data.

        Returns:
            dict: A dict of total character and unicode of a DataFrame.
        """
        total_characters = 0
        characters = ""
        for row in data:
            values = list(row.values())
            for value in values:
                if isinstance(value, str):
                    value = re.sub(r"[^a-zA-Z]", "", value)
                    total_characters += len(value)
                    characters += value

        characters = "".join(set(characters))

        return {
            "characters": total_characters,
            "unicode": len(characters),
        }

#!/usr/bin/env python3

# Copyright (C) Free Software Foundation, Inc. All rights reserved.
# Licensed under the AGPL-3.0-only License. See LICENSE in the project root
# for license information.

"""Library data quality for data profling."""

import re
import math
import statistics

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
            data (list): A list of data.

        Returns:
            int: A integer containing the total number of rows.
        """
        count = len(data)
        return count

    @staticmethod
    def check_duplicate_rows(data: list) -> int:
        """
        Check the number of duplicate rows in a given list of data.

        Args:
            data (list): A list of data.

        Returns:
            int: An integer containing the total number of duplicate.
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
        Generate sample of first and last 5 rows of list of data.

        Args:
            data (list): A list of data.

        Returns:
            dict: A dictionary of first and last 5 rows of data.
        """
        head, tail = data[:5], data[-5:]

        return head, tail

    @staticmethod
    def check_number_of_variables(data: list) -> int:
        """
        Generate the number of variables in a given list of data.

        Args:
            data (list): A list of data.

        Returns:
            int: A integer containing the total number of key.
        """
        count = len(data[0].keys())
        return count

    @staticmethod
    def check_missing_cells(data: list) -> int:
        """
        Check any missing cells of list of data.

        Args:
            data (list): A list of data.

        Returns:
            int: An int of total missing cells of list of data.
        """
        missing_cells = 0
        for row in data:
            value = list(row.values())
            value = [a.strip() if isinstance(a, str) else a for a in value]
            value = [
                (
                    ""
                    if (isinstance(a, float) or isinstance(a, int))
                    and str(a).lower() == "nan"
                    else a
                )
                for a in value
            ]

            missing_cells += sum(
                1 if r == "" or r is None else 0 for r in value
            )

        return missing_cells

    @staticmethod
    def check_characters_and_unicode(data: list) -> dict:
        """
        Check total characters and unicode of list of data.

        Args:
            data (list): A list of data.

        Returns:
            dict: A dict of total character and unicode a list of data.
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

    @staticmethod
    def check_data_types(data: list) -> dict:
        """
        Check data type of of list of data.

        Args:
            data (list): A list of data.

        Returns:
            dict: A dict of data type
        """
        data_types = {}

        for dictionary in data:
            for key, value in dictionary.items():
                current_type = type(value)
                if key not in data_types:
                    data_types[key] = set([current_type])
                else:
                    data_types[key].add(current_type)

        for key, value in data_types.items():
            if len(value) == 1:
                if list(value)[0] == str:
                    data_types[key] = "Text"
                elif list(value)[0] == bool:
                    data_types[key] = "Boolean"
                elif list(value)[0] == int or list(value)[0] == float:
                    data_types[key] = "Numeric"
                else:
                    data_types[key] = "Unkown"
            else:
                data_types[key] = "Unkown"
        return data_types

    def profiling(self):
        data = self.dataFrame.to_dict(orient="records")
        result = {
            "overview": {
                "number_of_observations": self.check_number_of_observations(
                    data
                ),
                "number_of_variables": self.check_number_of_variables(data),
                "missing_cells": self.check_missing_cells(data),
                "duplicate_rows": self.check_duplicate_rows(data),
                "data_types": self.check_data_types(data),
            },
            "sample": {
                "head": self.check_head_and_tail(data)[0],
                "tail": self.check_head_and_tail(data)[1],
            },
        }
        return result

    @staticmethod
    def check_max(data: list) -> float:
        """
        Check the highest number or maximum value of a list data.

        Args:
            data (list): A list of data.

        Returns:
            float: A float containing the total number of rows.
        """

        result = max(data)
        return result

    @staticmethod
    def check_min(data: list) -> float:
        """
        Check the lowest number or manimum value of a list data.

        Args:
            data (list): A list of data.

        Returns:
            float: A float containing the total number of rows.
        """
        result = min(data)
        return result

    @staticmethod
    def check_quantile(data: list, percentile: float) -> float:
        """
        Check a set of "cut points" that divides a numerical variable
        into groups containing the same number of observations.

        Args:
            data (list): A list of data.
            percentile(float) : Value at a particular percentile of a data set.
            Quantile 1 (Q1) : has a percentile value of 0.25
            Quantile 2 (Q2) : has a percentile value of 0.5
            Quantile 3 (Q3) : has a percentile value of 0.75

        Returns:
            float: A float containing the total number of rows.
        """
        n = len(data)
        idx = n * percentile / 100
        result = sorted(data)[math.floor(idx)]
        return result

    @staticmethod
    def check_median(data: list) -> float:
        """
        Check the the value in the middle of a series of values arranged
        in sequential data from small to large.

        Args:
            data (list): A list of data.

        Returns:
            float: A float containing the total number of rows.
        """
        result = statistics.median(data)
        return result

    @staticmethod
    def check_sum(data: list) -> float:
        """
        Generate sum of list of numeric values.

        Args:
            data (list): A list of numeric values.

        Returns:
            float: Sum result in float.
        """
        result = sum(data)
        return result

    @staticmethod
    def check_mean(data: list) -> dict:
        """
        Generate mean of numeric columns.

        Args:
            data (list): A list of data.

        Returns:
            dict: A dict of mean.
        """
        result = {}
        count = {}
        for row in data:
            for key, value in row.items():
                if isinstance(value, (int, float)):
                    result[key] = result.get(key, 0) + value
                    count[key] = count.get(key, 0) + 1
                elif key not in result:
                    result[key] = "Invalid Data Type"
                    count[key] = 0

        for key in result.keys():
            if isinstance(result[key], (int, float)):
                result[key] /= count[key] if count[key] != 0 else 1

        return result

    @staticmethod
    def check_std_dev(data: list) -> dict:
        """
        Generate standard deviation of numeric columns.

        Args:
            data (list): A list of data.

        Returns:
            dict: A dict of standard deviation.
        """
        result = {}
        count = {}
        sum_squared_diff = {}

        for row in data:
            for key, value in row.items():
                if isinstance(value, (int, float)):
                    result[key] = result.get(key, 0) + value
                    count[key] = count.get(key, 0) + 1
                    mean = result[key] / count[key]
                    squared_diff = (value - mean) ** 2
                    sum_squared_diff[key] = (
                        sum_squared_diff.get(key, 0) + squared_diff
                    )
                elif key not in result:
                    result[key] = "Invalid Data Type"
                    count[key] = 0
                    sum_squared_diff[key] = 0

        for key in result.keys():
            if isinstance(result[key], (int, float)):
                if count[key] > 1:
                    result[key] = math.sqrt(
                        sum_squared_diff[key] / (count[key] - 1)
                    )
                else:
                    result[key] = "Insufficient Data Points"

        return result

    @staticmethod
    def check_coeff_var(data: list) -> dict:
        """
        Generate coefficient variations of numeric columns.

        Args:
            data (list): A list of data.

        Returns:
            dict: A dict of coefficient variations.
        """
        result = {}
        count = {}
        sum_squared_diff = {}

        for row in data:
            for key, value in row.items():
                if isinstance(value, (int, float)):
                    result[key] = result.get(key, 0) + value
                    count[key] = count.get(key, 0) + 1
                    mean = result[key] / count[key]
                    squared_diff = (value - mean) ** 2
                    sum_squared_diff[key] = (
                        sum_squared_diff.get(key, 0) + squared_diff
                    )
                elif key not in result:
                    result[key] = "Invalid Data Type"
                    count[key] = 0
                    sum_squared_diff[key] = 0

        for key in result.keys():
            if isinstance(result[key], (int, float)):
                if count[key] > 1:
                    std_dev = math.sqrt(
                        sum_squared_diff[key] / (count[key] - 1)
                    )
                    mean = result[key] / count[key]
                    result[key] = (std_dev / mean) * 100
                else:
                    result[key] = "Insufficient Data Points"

        return result

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
                    data_types[key] = 'Text'
                elif list(value)[0] == bool:
                    data_types[key] = 'Boolean'
                elif list(value)[0] == int or list(value)[0] == float:
                    data_types[key] = 'Numeric'
                else:
                    data_types[key] = 'Unkown'
            else:
                data_types[key] = 'Unkown'
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
                "data_types": self.check_data_types(data)
            },
            "sample": {
                "head": self.check_head_and_tail(data)[0],
                "tail": self.check_head_and_tail(data)[1],
            },
        }
        return result

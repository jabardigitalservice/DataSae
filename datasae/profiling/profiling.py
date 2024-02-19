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

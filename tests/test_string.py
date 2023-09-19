#!/usr/bin/env python3

# This module is part of DataSae and is released under
# the AGPL-3.0-only License: https://opensource.org/license/agpl-v3/

import unittest

from datasae.string import String
import pandas


class StringTestCase(unittest.TestCase):
    """Class for unit testing datasae string"""

    def initialize(self):
        """
        initialize parameter to be tested
        :param:
        :return: dataframe pandas
        """
        data = [
            {"column_1": "this is a string", "column_2": 34},
            {"column_1": None, "column_2": "do job"},
        ]
        df = pandas.DataFrame.from_dict(data)

        return df

    def test_init(self):
        """
        testing init value of datasae string
        :return: assert equal result
        """
        results = {"score": 0, "message": []}

        obj = String(self.initialize())
        self.assertEqual(obj.results, results)

    def test_is_dataframe_true(self):
        """
        testing function is_dataframe datasae string
        :return: assert equal result
        """

        obj = String(self.initialize())
        self.assertEqual(obj.is_dataframe(), True)

    def test_is_dataframe_false(self):
        """
        testing function is_dataframe datasae string
        :return: assert equal result
        """

        obj = String(123)
        self.assertEqual(obj.is_dataframe(), False)

#!/usr/bin/env python3

# This module is part of DataSae and is released under
# the AGPL-3.0-only License: https://opensource.org/license/agpl-v3/

import unittest

import numpy as np
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point, LineString, Polygon


from datasae.geospatial import Geospatial, WarningDataDetailMessage
from datasae.utils import create_warning_data, WarningDataMessage

from . import MESSAGE


class GeospatialTest(unittest.TestCase):
    def __init__(self, methodName: str = 'TestGeospatial'):
        super().__init__(methodName)
        self.maxDiff = None

    def test_point(self):
        point_type = Point(2, 1)
        data = {'geometry': [point_type]}
        dummy = gpd.GeoDataFrame(data, geometry='geometry')

        actual_result = Geospatial(dummy).point(point_type, 'geometry')
        # print(actual_result)
        excepted_result = {
            'score': 1.,
            'valid': 1,
            'invalid': 0,
            'warning': {}
        }

        self.assertDictEqual(actual_result, excepted_result, MESSAGE)
    
    def test_polyline(self):
        polyline_type = LineString([(1, 1), (2, 1)])
        data = {'geometry': [polyline_type]}
        dummy = gpd.GeoDataFrame(data, geometry='geometry')

        # Calculate the actual result
        geospatial = Geospatial(dummy)
        actual_result = geospatial.polyline(polyline_type, 'geometry')

        # Define the expected result
        expected_result = {
            'score': 1.0,
            'valid': 1,
            'invalid': 0,
            'warning': {}
        }

        # Assert that the actual result matches the expected result
        self.assertDictEqual(actual_result, expected_result, "Result Not Match")

    def test_polygon(self):
        polygon_type = Polygon([(0, 0), (1, 0), (1, 1), (0, 1)])
        data = {'geometry': [polygon_type]}
        dummy = gpd.GeoDataFrame(data, geometry='geometry')

        actual_result = Geospatial(dummy).polygon(polygon_type, 'geometry')
        # print(actual_result)
        excepted_result = {
            'score': 1.,
            'valid': 1,
            'invalid': 0,
            'warning': {}
        }

        self.assertDictEqual(actual_result, excepted_result, MESSAGE)
        
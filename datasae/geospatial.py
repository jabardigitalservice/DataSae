#!/usr/bin/env python3

# This module is part of DataSae and is released under
# the AGPL-3.0-only License: https://opensource.org/license/agpl-v3/

import pandas as pd
import geopandas as gpd
from shapely.geometry import Point, LineString, Polygon
from .exception import InvalidDataTypeWarning, InvalidDataValueWarning
from .utils import Basic, create_warning_data, WarningDataMessage


class WarningDataDetailMessage:
    GEOSPATIAL_DATA_TYPE: str = "Value must be of geospatial data type"


class Geospatial(Basic):
    def __init__(self, dataFrame: pd.DataFrame):
        """
        Initializes an instance of the Integer class.

        Args:
            dataFrame (pd.DataFrame): The data you want to process.
        """

        self.dataFrame = dataFrame

    @staticmethod
    def check_point(point_data: Point, value: Point) -> tuple:
        """
        Check if a given point value is equal to a specified value.

        Args:
            point_data (Point): Point value to be checked.
            value (Point): The specified value to compare against.

        Returns:
            tuple: A tuple containing the following elements:
                - valid (int): The number of valid values (either 0 or 1).
                - invalid (int): The number of invalid values (either 0 or 1).
                - warning_data (dict): A dictionary with warning data if the
                    value is invalid, including the warning message,
                    the actual value, and a detailed message.
        """

        valid = 0
        invalid = 0
        warning_data = {}

        if point_data == value:
            valid = 1
        else:
            invalid = 1
            warning_data = create_warning_data(
                point_data, f"Value should be equal to {value}"
            )

        return valid, invalid, warning_data

    @staticmethod
    def check_polyline(polyline_data: LineString, value: LineString) -> tuple:
        """
        Check if a given integer value is equal to a specified value.

        Args:
            integer_data (int): The integer value to be checked.
            value (int): The specified value to compare against.

        Returns:
            tuple: A tuple containing the following elements:
                - valid (int): The number of valid values (either 0 or 1).
                - invalid (int): The number of invalid values (either 0 or 1).
                - warning_data (dict): A dictionary with warning data if the
                    value is invalid, including the warning message,
                    the actual value, and a detailed message.
        """

        valid = 0
        invalid = 0
        warning_data = {}

        if polyline_data == value:
            valid = 1
        else:
            invalid = 1
            warning_data = create_warning_data(
                polyline_data, f"Value should be equal to {value}"
            )

        return valid, invalid, warning_data

    @staticmethod
    def check_polygon(polygon_data: Polygon, value: Polygon) -> tuple:
        """
        Check if a given polygon value is equal to a specified value.

        Args:
            polygon_data (Polygon): polygon value to be checked.
            value (Polygon): The specified value to compare against.

        Returns:
            tuple: A tuple containing the following elements:
                - valid (int): The number of valid values (either 0 or 1).
                - invalid (int): The number of invalid values (either 0 or 1).
                - warning_data (dict): A dictionary with warning data if the
                    value is invalid, including the warning message,
                    the actual value, and a detailed message.
        """

        valid = 0
        invalid = 0
        warning_data = {}

        if polygon_data == value:
            valid = 1
        else:
            invalid = 1
            warning_data = create_warning_data(
                polygon_data, f"Value should be equal to {value}"
            )

        return valid, invalid, warning_data

    def point(self, value: Point, column: str) -> dict:
        """
        Check if the values in a specified column of a DataFrame are equal to
            a given value.

        Args:
            value (Point): The value to compare the column values against.
            column (str): The name of the column in the DataFrame to check.

        Returns:
            dict: A dictionary containing the result of the data quality check,
                including the number of valid and invalid values,
                and any warning messages.
        """

        valid = 0
        invalid = 0
        warning = {}

        for index, point_data in enumerate(self.dataFrame[column]):
            try:
                if isinstance(point_data, (Point)) is False:
                    raise InvalidDataTypeWarning(warning)

                valid_row, invalid_row, warning_data = self.check_point(
                    point_data, value
                )
                valid += valid_row
                invalid += invalid_row

                if warning_data != {}:
                    warning[index] = InvalidDataValueWarning(
                        warning_data
                    ).message
            except InvalidDataTypeWarning:
                invalid += 1
                warning_data = create_warning_data(
                    point_data,
                    WarningDataDetailMessage.GEOSPATIAL_DATA_TYPE,
                    WarningDataMessage.INVALID_DATA_TYPE,
                )
                warning[index] = InvalidDataTypeWarning(warning_data).message

        result = self.response(valid, invalid, warning)
        return result

    def polyline(self, value: LineString, column: str) -> dict:
        """
        Check if the values in a specified column of a DataFrame are equal to
            a given value.

        Args:
            value (int): The value to compare the column values against.
            column (str): The name of the column in the DataFrame to check.

        Returns:
            dict: A dictionary containing the result of the data quality check,
                including the number of valid and invalid values,
                and any warning messages.
        """

        valid = 0
        invalid = 0
        warning = {}

        for index, polyline_data in enumerate(self.dataFrame[column]):
            try:
                if isinstance(polyline_data, (LineString)) is False:
                    raise InvalidDataTypeWarning(warning)

                valid_row, invalid_row, warning_data = self.check_polyline(
                    polyline_data, value
                )
                valid += valid_row
                invalid += invalid_row

                if warning_data != {}:
                    warning[index] = InvalidDataValueWarning(
                        warning_data
                    ).message
            except InvalidDataTypeWarning:
                invalid += 1
                warning_data = create_warning_data(
                    polyline_data,
                    WarningDataDetailMessage.GEOSPATIAL_DATA_TYPE,
                    WarningDataMessage.INVALID_DATA_TYPE,
                )
                warning[index] = InvalidDataTypeWarning(warning_data).message

        result = self.response(valid, invalid, warning)
        return result

    def polygon(self, value: Polygon, column: str) -> dict:
        """
        Check if the values in a specified column of a DataFrame are equal to
            a given value.

        Args:
            value (Polygon): The value to compare the column values against.
            column (str): The name of the column in the DataFrame to check.

        Returns:
            dict: A dictionary containing the result of the data quality check,
                including the number of valid and invalid values,
                and any warning messages.
        """

        valid = 0
        invalid = 0
        warning = {}

        for index, polygon_data in enumerate(self.dataFrame[column]):
            try:
                if isinstance(polygon_data, (Polygon)) is False:
                    raise InvalidDataTypeWarning(warning)

                valid_row, invalid_row, warning_data = self.check_polygon(
                    polygon_data, value
                )
                valid += valid_row
                invalid += invalid_row

                if warning_data != {}:
                    warning[index] = InvalidDataValueWarning(
                        warning_data
                    ).message
            except InvalidDataTypeWarning:
                invalid += 1
                warning_data = create_warning_data(
                    polygon_data,
                    WarningDataDetailMessage.GEOSPATIAL_DATA_TYPE,
                    WarningDataMessage.INVALID_DATA_TYPE,
                )
                warning[index] = InvalidDataTypeWarning(warning_data).message

        result = self.response(valid, invalid, warning)
        return result

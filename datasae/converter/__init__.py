#!/usr/bin/env python3

# Copyright (c) Free Software Foundation, Inc. All rights reserved.
# Licensed under the AGPL-3.0-only License. See LICENSE in the project root
# for license information.

"""
Converter library.

A class called `Config` that represents a configuration object for reading
data source configurations from a JSON or YAML file.
"""

from __future__ import annotations
from dataclasses import dataclass
from enum import Enum
from io import BytesIO, StringIO
import json
from pathlib import Path
from typing import Callable
import warnings

import pandas as pd
import yaml


class CaseInsensitiveEnum(str, Enum):
    """
    A case-insensitive enumeration class.

    A case-insensitive enumeration class that allows for case-insensitive
    comparison of enum values and provides a case-insensitive lookup of enum
    members.
    """

    def __eq__(self, __value: str) -> bool:
        """
        __eq__ methods.

        Overrides the __eq__ method to perform case-insensitive comparison of
        enum values.

        Args:
            __value (str): The value to compare with the enum value.

        Returns:
            bool: True if the values are equal (case-insensitive), False
                otherwise.
        """
        return super().__eq__(__value.lower() if __value else __value)

    @classmethod
    def _missing_(cls, value: str) -> CaseInsensitiveEnum:
        """
        _missing_ method.

        Overrides the _missing_ method to perform case-insensitive lookup of
            enum members.

        Args:
            value (str): The value to lookup in the enum members.

        Returns:
            CaseInsensitiveEnum: The enum member with the matching value (case-
                insensitive).
        """
        value = value.lower() if value else value

        for member in cls:
            if member.value.lower() == value:
                return member


class FileType(CaseInsensitiveEnum):
    """
    FileType enumeration.

    Represents different types of file formats with case-insensitive
    comparison and lookup of enum values.
    """

    CSV = '.csv'
    JSON = '.json'
    PARQUET = '.parquet'
    SQL = '.sql'
    YAML = '.yaml'
    YML = '.yml'
    XLSX = '.xlsx'


class DataSourceType(CaseInsensitiveEnum):
    """
    DataSourceType enumeration.

    Represents a case-insensitive enumeration for different types of data
    sources.
    """

    S3 = 's3'
    POSTGRESQL = 'postgresql'


@dataclass(repr=False)
class DataSource:
    """
    DataSource class.

    A class that converts data of different file types into a Pandas DataFrame.
    """

    type: DataSourceType

    @property
    def connection(self) -> dict:
        """
        Return connection to data source.

        Returns:
            dict: Key-value parameters for connection to datasource.
        """
        return {
            key: value
            for key, value in self.__dict__.items()
            if key != 'type'
        }

    def __call__(
        self, file_type: FileType, data: bytes | str, *args, **kwargs
    ) -> pd.DataFrame | bytes:
        """
        __call__ method.

        Converter from various file type into Pandas DataFrame.

        Args:
            file_type (FileType): _description_
            data (bytes | str): Data's bytes or sql query needed convert to
                dataframe.

        Returns:
            DataFrame | bytes: Pandas DataFrame or bytes if file type not
                support.
        """
        if file_type in list(FileType):
            func: Callable = None

            if file_type is FileType.CSV:
                func = pd.read_csv
            elif file_type is FileType.JSON:
                func = pd.read_json
            elif file_type is FileType.PARQUET:
                func = pd.read_parquet
            elif file_type is FileType.XLSX:
                func = pd.read_excel
            elif file_type is FileType.SQL:
                func = pd.read_sql_query

            if func:
                with warnings.catch_warnings(record=True):
                    warnings.simplefilter('always')
                    if file_type is FileType.SQL:
                        data = func(data, self.connection, *args, **kwargs)
                    else:
                        data = func(
                            StringIO(data.decode())
                            if file_type in (FileType.CSV, FileType.JSON)
                            else BytesIO(data),
                            *args,
                            **kwargs
                        )

        return data


class Config:
    """
    A class that represents a configuration object.

    Args:
        file_path (str): The source path of the .json or .yaml file.

    Example Usage:
        config = Config("data.json")
        data_source = config("source1")
        print(data_source.connection)

    Attributes:
        __file (str): The source path of the file.
        __file_type (str): The type of the file.

    Methods:
        __call__(name):
            Returns a data source configuration from a file.

    """

    def __init__(self, file_path: str):
        """
        __init__ method.

        Initializes an instance of the Converter Configuration.

        Args:
            file_path (str): Source path of your .json or .yaml file.
        """
        self.__file: Path = Path(file_path)
        self.__file_type: FileType = FileType(self.__file.suffix)

    def __call__(self, name: str) -> DataSource:
        """
        Return data source configuration from file.

        Args:
            name (str): Name of data source.

        Returns:
            DataSource: An instance class of data source containing
                configuration properties.
        """
        config: dict = {}

        with open(self.__file) as file:
            if self.__file_type is FileType.JSON:
                config = json.loads(file.read())
            elif self.__file_type in (FileType.YAML, FileType.YML):
                config = yaml.safe_load(file)

        data_source: dict = {
            key: DataSourceType(value) if key == 'type' else value
            for key, value in config.get(name, {}).items()
        }
        source_type: DataSourceType = data_source['type']

        if source_type is DataSourceType.S3:
            from .s3 import S3

            return S3(**data_source)
        elif source_type is DataSourceType.POSTGRESQL:
            from .postgresql import PostgreSQL

            return PostgreSQL(**data_source)

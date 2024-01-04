#!/usr/bin/env python3

# Copyright (C) Free Software Foundation, Inc. All rights reserved.
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
import logging
import json
from pathlib import Path
from pydoc import locate
from typing import Any, Callable
import warnings

import pandas as pd
import yaml

from ..boolean import Boolean
from ..float import Float
from ..integer import Integer
from ..string import String
from ..timestamp import Timestamp


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


@dataclass(repr=False)
class DataSource:
    """
    DataSource class.

    A class that converts data of different file types into a Pandas DataFrame.
    """

    name: str
    file_path: str

    @property
    def checker(self) -> list[dict]:
        """
        Checker is instance's attribute.

        Creates a list of checker result based on the configuration provided
        in the checker section of the data source's configuration file.
        """
        checker_list: list[dict] = Config.config(
            self.file_path
        )[self.name].get('checker', [])

        for checker in checker_list:
            data: pd.DataFrame = self(**{
                key: value
                for key, value in checker.items()
                if key != 'column'
            })

            for column_name, data_type_list in checker['column'].items():
                for data_type, rules in data_type_list.items():
                    try:
                        check_data: Any = {
                            'boolean': Boolean,
                            'float': Float,
                            'integer': Integer,
                            'string': String,
                            'timestamp': Timestamp
                        }.get(
                            data_type.lower(),
                            locate(data_type)
                        )(data)
                    except ModuleNotFoundError:  # pragma: no cover
                        logging.error(
                            'Please run this on your terminal:'
                        )  # pragma: no cover
                        logging.error(
                            "pip install 'DataSae[converter]'"
                        )  # pragma: no cover
                        raise  # pragma: no cover

                    for method_name, params in rules.items():
                        method = getattr(check_data, method_name)
                        rules[method_name] = dict(
                            params=params,
                            result=method(**params, column=column_name)
                            if isinstance(params, dict)
                            else method(
                                *(
                                    params
                                    if isinstance(params, list)
                                    else ([params] if params else [])
                                ),
                                column=column_name
                            )
                        )

        return checker_list

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
            if key not in DataSource.__annotations__.keys()
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
            elif file_type is FileType.SQL:
                func = pd.read_sql_query
            elif file_type is FileType.XLSX:
                func = pd.read_excel

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


@dataclass
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

    file_path: str

    @staticmethod
    def config(file_path: str) -> dict:
        """
        Config.config static method.

        Reads a file and returns its contents as a dictionary.

        Args:
            file_path (str): Source path of your .json or .yaml file.

        Returns:
            dict: The contents of the file as a dictionary.
        """
        file: Path = Path(file_path)
        file_type: FileType = FileType(file.suffix)
        data: dict = {}

        with open(file) as file_obj:
            if file_type is FileType.JSON:
                data = json.loads(file_obj.read())
            elif file_type in (FileType.YAML, FileType.YML):
                data = yaml.safe_load(file_obj)

        return data

    def __call__(self, name: str) -> DataSource:
        """
        Return data source configuration from file.

        Args:
            name (str): Name of data source.

        Returns:
            DataSource: An instance class of data source containing
                configuration properties.
        """
        data_source: dict = {
            'name': name,
            'file_path': self.file_path,
            **{
                key: value
                for key, value in Config.config(
                    self.file_path
                ).get(name, {}).items()
                if key != 'checker'
            }
        }
        data_source_type: str = data_source.pop('type')

        if data_source_type.lower() == 'local':
            try:
                from .local import Local
            except ModuleNotFoundError:  # pragma: no cover
                logging.error(
                    'Please run this on your terminal:'
                )  # pragma: no cover
                logging.error(
                    "pip install 'DataSae[converter]'"
                )  # pragma: no cover
                raise  # pragma: no cover

            data_source_type = Local
        elif data_source_type.lower() == 'gsheet':
            try:
                from .gsheet import GSheet
            except ModuleNotFoundError:  # pragma: no cover
                logging.error(
                    'Please run this on your terminal:'
                )  # pragma: no cover
                logging.error(
                    "pip install 'DataSae[converter,gsheet]'"
                )  # pragma: no cover
                raise  # pragma: no cover

            data_source_type = GSheet
        elif data_source_type.lower() == 's3':
            try:
                from .s3 import S3
            except ModuleNotFoundError:  # pragma: no cover
                logging.error(
                    'Please run this on your terminal:'
                )  # pragma: no cover
                logging.error(
                    "pip install 'DataSae[converter,s3]'"
                )  # pragma: no cover
                raise  # pragma: no cover

            data_source_type = S3
        elif data_source_type.lower() == 'sql':
            try:
                from .sql import Sql
            except ModuleNotFoundError:  # pragma: no cover
                logging.error(
                    'Please run this on your terminal:'
                )  # pragma: no cover
                logging.error(
                    "pip install 'DataSae[converter,sql]'"
                )  # pragma: no cover
                raise  # pragma: no cover

            data_source_type = Sql
        else:
            try:
                # Dynamic instantiation from string name of a class in
                # dynamically imported module?
                # https://stackoverflow.com/questions/4821104/dynamic-instantiation-from-string-name-of-a-class-in-dynamically-imported-module
                data_source_type = locate(data_source_type)
            except ModuleNotFoundError:  # pragma: no cover
                logging.error(
                    'Please run this on your terminal:'
                )  # pragma: no cover
                logging.error(
                    "pip install 'DataSae[converter,gsheet,s3,sql]'"
                )  # pragma: no cover
                raise  # pragma: no cover

        return data_source_type(**data_source)

    @property
    def checker(self) -> dict[str, list[dict]]:
        """
        Checker is instance's attribute.

        Creates all of checker result based on the configuration provided
        in the checker section of the data source's configuration file.
        """
        return {
            name: self(name).checker
            for name in self.config(self.file_path).keys()
        }

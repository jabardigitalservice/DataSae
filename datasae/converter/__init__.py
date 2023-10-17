#!/usr/bin/env python3

# Copyright (c) Free Software Foundation, Inc. All rights reserved.
# Licensed under the AGPL-3.0-only License. See LICENSE in the project root
# for license information.

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
    def __eq__(self, __value: str) -> bool:
        return super().__eq__(__value.lower() if __value else __value)

    @classmethod
    def _missing_(cls, value: str) -> CaseInsensitiveEnum:
        value = value.lower() if value else value

        for member in cls:
            if member.value.lower() == value:
                return member


class FileType(CaseInsensitiveEnum):
    CSV = '.csv'
    JSON = '.json'
    PARQUET = '.parquet'
    YAML = '.yaml'
    YML = '.yml'
    XLSX = '.xlsx'


class DataSourceType(CaseInsensitiveEnum):
    MINIO = 'minio'


@dataclass(repr=False)
class DataSource:
    type: DataSourceType

    @property
    def connection(self) -> dict:
        '''
        Return connection to data source.

        Returns:
            dict: _description_
        '''

        return {
            key: value
            for key, value in self.__dict__.items()
            if key != 'type'
        }

    def __call__(
        self, file_type: FileType, data: bytes, *args, **kwargs
    ) -> pd.DataFrame | bytes:
        '''
        Converter from various file type into Pandas DataFrame.

        Args:
            file_type (FileType): _description_
            data (bytes): _description_

        Returns:
            DataFrame | bytes: Pandas DataFrame or bytes if file type not
                support.
        '''

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

            if func:
                with warnings.catch_warnings(record=True):
                    warnings.simplefilter('always')
                    data = func(
                        StringIO(data.decode())
                        if file_type in (FileType.CSV, FileType.JSON)
                        else BytesIO(data),
                        *args,
                        **kwargs
                    )

        return data


class Config:
    def __init__(self, file_path: str):
        '''
        Initializes an instance of the Converter Configuration.

        Args:
            file_path (str): Source path of your .json or .yaml file.
        '''

        self.__file: Path = Path(file_path)
        self.__file_type: FileType = FileType(self.__file.suffix)

    def __call__(self, name: str) -> DataSource:
        '''
        Return data source configuration from file.

        Args:
            name (str): Name of data source.

        Returns:
            DataSource: An instance class of data source containing
                configuration properties.
        '''

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

        if source_type is DataSourceType.MINIO:
            from .minio import Minio

            return Minio(**data_source)

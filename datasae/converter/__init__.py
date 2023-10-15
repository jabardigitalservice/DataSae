#!/usr/bin/env python3

# Copyright (c) Free Software Foundation, Inc. All rights reserved.
# Licensed under the AGPL-3.0-only License. See LICENSE in the project root
# for license information.

from __future__ import annotations
from dataclasses import dataclass
from enum import Enum
import json
from pathlib import Path
from typing import Any

from pandas import DataFrame
import yaml


class CaseInsensitiveEnum(str, Enum):
    def __eq__(self, __value: str) -> bool:
        return super().__eq__(__value.lower())

    @classmethod
    def _missing_(cls, value: str) -> CaseInsensitiveEnum:
        value = value.lower()

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

    def connection(self) -> Any:
        '''
        Return connection to data source.

        Returns:
            Any: Instance class for connection to data source.
        '''

        pass

    def read(self) -> DataFrame:
        '''
        Converter from various file type into Pandas DataFrame.

        Returns:
            DataFrame: Pandas DataFrame.
        '''

        pass


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
            Any: An instance class of data source containing configuration
                properties.
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

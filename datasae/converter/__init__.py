#!/usr/bin/env python3

# Copyright (c) Free Software Foundation, Inc. All rights reserved.
# Licensed under the AGPL-3.0-only License. See LICENSE in the project root
# for license information.

from dataclasses import dataclass
from enum import Enum
import json
from pathlib import Path
from typing import Any

import yaml


class FileType(str, Enum):
    JSON = '.json'
    YAML = '.yaml'
    YML = '.yml'


class DataSourceType(str, Enum):
    MINIO = 'minio'


@dataclass(repr=False)
class DataSource:
    type: DataSourceType

    def connection(self):
        pass

    def read(self):
        pass


class Config:
    def __init__(self, file_path: str):
        self.__file: Path = Path(file_path)
        self.__file_type: FileType = FileType(self.__file.suffix.lower())

    def __call__(self, name: str) -> Any:
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

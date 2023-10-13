#!/usr/bin/env python3

# Copyright (c) Free Software Foundation, Inc. All rights reserved.
# Licensed under the AGPL-3.0-only License. See LICENSE in the project root
# for license information.

from dataclasses import make_dataclass
from enum import Enum
import json
from pathlib import Path
from typing import Any

import yaml


class DataSourceType(str, Enum):
    MINIO = 'minio'


def connection(self):
    if self.type == DataSourceType.MINIO:
        from .connection.minio import Minio

        Minio()


def reader(self):
    print(self.type)


class Config:
    def __init__(self, file_path: str):
        self.__file: str = Path(file_path)

    def __call__(self, name: str) -> Any:
        config: dict = {}
        file_type: str = self.__file.suffix.lower()

        with open(self.__file) as file:
            if file_type == '.json':
                config = json.loads(file.read())
            elif file_type in ('.yaml', '.yml'):
                config = yaml.safe_load(file)

        data_source = config.get(name, {})

        return make_dataclass(
            'DataSource',
            (
                (key, DataSourceType) if key == 'type' else key
                for key in data_source.keys()
            ),
            namespace=dict(
                connection=connection,
                reader=reader
            )
        )(**{
            key: DataSourceType(value) if key == 'type' else value
            for key, value in data_source.items()
        })

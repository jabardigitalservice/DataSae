#!/usr/bin/env python3

# Copyright (c) Free Software Foundation, Inc. All rights reserved.
# Licensed under the AGPL-3.0-only License. See LICENSE in the project root
# for license information.

from __future__ import annotations
from dataclasses import dataclass
from pandas import DataFrame
from urllib3 import BaseHTTPResponse

from minio import Minio as MinioClass

from . import DataSource, FileType


@dataclass(repr=False)
class Minio(DataSource):
    endpoint: str
    access_key: str
    secret_key: str

    @property
    def connection(self) -> MinioClass:
        return MinioClass(**super().connection)

    def __call__(self, *args, **kwargs) -> DataFrame | bytes:
        response: BaseHTTPResponse = self.connection.get_object(
            *args, **kwargs
        )
        data: bytes = response.data
        content_type: str = response.headers.get('Content-Type')
        response.close()
        response.release_conn()
        file_type: FileType = None

        if content_type == 'text/csv':
            file_type = FileType.CSV
        elif content_type == 'application/json':
            file_type = FileType.JSON
        elif content_type == 'application/octet-stream':
            file_type = FileType.PARQUET
        elif content_type == (
            'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        ):
            file_type = FileType.XLSX

        return super().__call__(file_type, data)

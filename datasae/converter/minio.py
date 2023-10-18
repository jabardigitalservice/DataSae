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

    def __call__(
        self, bucket_name: str, object_name: str, *args, **kwargs
    ) -> DataFrame | bytes:
        '''
        Converter from various file type into Pandas DataFrame.

        Args:
            bucket_name (str): _description_
            object_name (str): _description_

        Returns:
            DataFrame | bytes: Pandas DataFrame or bytes if file type not
                support.
        '''

        sheet_name: int | str = kwargs.pop('sheet_name', None)
        response: BaseHTTPResponse = self.connection.get_object(
            bucket_name, object_name, *args, **kwargs
        )
        kwargs = {}

        if sheet_name:
            kwargs['sheet_name'] = sheet_name

        data: DataFrame | bytes = super().__call__(
            {
                'text/csv': FileType.CSV,
                'application/json': FileType.JSON,
                'application/octet-stream': FileType.PARQUET,
                'application/vnd.openxmlformats-officedocument.spreadsheetml.'
                'sheet': FileType.XLSX
            }.get(response.headers.get('Content-Type')),
            response.data,
            **kwargs
        )
        response.close()
        response.release_conn()
        return data

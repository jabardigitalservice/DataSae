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
        self, file_type: FileType, *args, **kwargs
    ) -> DataFrame | bytes:
        '''
        Converter from various file type into Pandas DataFrame.

        Args:
            file_type (FileType): _description_

        Returns:
            DataFrame | bytes: Pandas DataFrame or bytes if file type not
                support.
        '''

        response: BaseHTTPResponse = self.connection.get_object(
            *args, **kwargs
        )
        data = response.data
        response.close()
        response.release_conn()
        return super().__call__(file_type, data)

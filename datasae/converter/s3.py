#!/usr/bin/env python3

# Copyright (C) Free Software Foundation, Inc. All rights reserved.
# Licensed under the AGPL-3.0-only License. See LICENSE in the project root
# for license information.

"""s3 library."""

from __future__ import annotations
from dataclasses import dataclass
from urllib3 import BaseHTTPResponse

from minio import Minio
from pandas import DataFrame

from . import DataSource, FileType


@dataclass(repr=False)
class S3(DataSource):
    """
    Represents a data source that connects to an S3 bucket.

    Args:
        endpoint (str): The endpoint URL of the S3 bucket.
        access_key (str): The access key for authentication.
        secret_key (str): The secret key for authentication.
        bucket_name (str, optional): The name of the S3 bucket.
    """

    endpoint: str
    access_key: str
    secret_key: str
    bucket_name: str = None

    @property
    def connection(self) -> Minio:
        """
        Returns a connection to the S3 bucket.

        Returns:
            minio.Minio: An instance of the Minio class.
        """
        return Minio(**{
            key: value
            for key, value in super().connection.items()
            if key != 'bucket_name'
        })

    def __call__(
        self, object_name: str, bucket_name: str = None, *args, **kwargs
    ) -> DataFrame | bytes:
        """
        __call__ method.

        Converts the data from the specified bucket and object name into a
        Pandas DataFrame.

        Args:
            object_name (str): The object name in the bucket.
            bucket_name (str, optional): The name of the S3 bucket.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Keyword Args:
            sheet_name (int | str, optional): This parameter only works for
                .xlsx files. Strings are used for sheet names. Integers are
                used for zero-indexed sheet positions (chart sheets do not
                count as a sheet position). Lists of strings/integers are used
                to request multiple sheets. Specify None to get all worksheets.
                Available cases:
                    - Defaults to None: 1st sheet as a DataFrame
                    - 0: 1st sheet as a DataFrame
                    - 1: 2nd sheet as a DataFrame
                    - "Sheet1": Load sheet with name "Sheet1"

        Returns:
            DataFrame | bytes: A Pandas DataFrame or bytes if the file type is
                not supported.
        """
        PARAMS: tuple = (
            'bucket_name',
            'object_name',
            'offset',
            'length',
            'request_headers',
            'ssec',
            'version_id',
            'extra_query_params'
        )
        response: BaseHTTPResponse = self.connection.get_object(
            bucket_name if bucket_name else self.bucket_name,
            object_name,
            *args,
            **{
                key: value
                for key, value in kwargs.items()
                if key in PARAMS
            }
        )

        data: DataFrame | bytes = super().__call__(
            {
                'text/csv': FileType.CSV,
                'application/json': FileType.JSON,
                'application/octet-stream': FileType.PARQUET,
                'application/vnd.openxmlformats-officedocument.spreadsheetml.'
                'sheet': FileType.XLSX
            }.get(response.headers.get('Content-Type')),
            response.data,
            **{
                key: value
                for key, value in kwargs.items()
                if key not in PARAMS
            }
        )
        response.close()
        response.release_conn()
        return data

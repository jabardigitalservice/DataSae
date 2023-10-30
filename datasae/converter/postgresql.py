#!/usr/bin/env python3

# Copyright (c) Free Software Foundation, Inc. All rights reserved.
# Licensed under the AGPL-3.0-only License. See LICENSE in the project root
# for license information.

"""postgresql library."""

from __future__ import annotations
from dataclasses import dataclass
import os

from pandas import DataFrame
from sqlalchemy import create_engine, Engine, URL

from . import DataSource, FileType


@dataclass(repr=False)
class PostgreSQL(DataSource):
    """
    Represents a data source that connects to a postgresql table.

    Args:
        host (str): The host of postgresql connection.
        port (int): The port of postgresql connection.
        database (str): The database name of postgresql connection.
        username (str): The username of postgresql connection.
        password (str): The password of postgresql connection.

    """

    host: str
    port: int
    database: str
    username: str
    password: str

    @property
    def connection(self) -> Engine:
        """
        Returns an engine connection to the postgresql.

        Returns:
            sqlalchemy.Engine: An instance of the sqlalchemy class.
        """
        return create_engine(
            URL.create('postgresql', **super().connection)
        )

    def __call__(self, query: str, *args, **kwargs) -> DataFrame | bytes:
        """
        __call__ method.

        Converts the data from the specified bucket and object name into a
        Pandas DataFrame.

        Args:
            bucket_name (str): The name of the bucket.
            object_name (str): The object name in the bucket.
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
        if os.path.isfile(query):
            with open(query) as file:
                query = file.read()

        return super().__call__(FileType.SQL, query, *args, **kwargs)

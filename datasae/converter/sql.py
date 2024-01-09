#!/usr/bin/env python3

# Copyright (C) Free Software Foundation, Inc. All rights reserved.
# Licensed under the AGPL-3.0-only License. See LICENSE in the project root
# for license information.

"""sql library."""

from __future__ import annotations
from dataclasses import dataclass
import os

from pandas import DataFrame
from sqlalchemy import create_engine, Engine, URL

from . import DataSource, FileType


@dataclass(repr=False)
class Sql(DataSource):
    """
    Represents a data source that connects to a sql table.

    Args:
        drivername (str): The name of the database backend.
        username (str): The username of sql connection.
        password (str): The password of sql connection.
        host (str): The host of sql connection.
        port (int): The port of sql connection.
        database (str): The database name of sql connection.
    """

    drivername: str
    username: str
    password: str
    host: str
    port: int
    database: str

    @property
    def connection(self) -> Engine:
        """
        Returns an engine connection to the sql.

        Returns:
            sqlalchemy.Engine: An instance of the sqlalchemy class.
        """
        return create_engine(
            URL.create(**super().connection)
        )

    def __call__(self, query: str, *args, **kwargs) -> DataFrame:
        """
        __call__ method.

        Converts the data from the defined sql query into a
        Pandas DataFrame.

        Args:
            query (str): Sql query.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            DataFrame: A Pandas DataFrame.
        """
        if os.path.isfile(query):
            with open(query) as file:
                query = file.read()

        return super().__call__(FileType.SQL, query, *args, **kwargs)

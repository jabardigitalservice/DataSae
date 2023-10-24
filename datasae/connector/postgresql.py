#!/usr/bin/env python3

# Copyright (c) Free Software Foundation, Inc. All rights reserved.
# Licensed under the AGPL-3.0-only License. See LICENSE in the project root
# for license information.

from dataclasses import dataclass
import pandas as pd

from sqlalchemy import create_engine as PostgresqlClass

from . import DataSource


@dataclass(repr=False)
class Postgresql(DataSource):
    username: str
    password: str
    host: str
    port: str
    name: str

    @property
    def connection(self) -> PostgresqlClass:
        """
        Return connection to data source.

        Returns:
            sqlalchemy.create_engine: Instance from library
                class sqlalchemy.create_engine's.
        """

        return PostgresqlClass(**super().connection)

    def read_table(
        self, schema_name: str, table_name: str
            ) -> pd.DataFrame | bytes:
        """
        Converter from postgresql table into Pandas DataFrame.

        Args:
            schema_name (str): name of the postgresql schema
            table_name (str): name of the postgresq table

        Returns:
            pd.DataFrame | bytes: Pandas DataFrame or bytes if file type not
                support.
        """

        query = f"select * from {schema_name}.{table_name};"

        data: pd.DataFrame | bytes = pd.read_sql_query(
            query, self.connection
        )

        return data

    def custom_query(
        self, schema_name: str, table_name: str, custom_query: str
            ) -> pd.DataFrame | bytes:
        """
        Converter from postgresql table into Pandas DataFrame
            with custom query.

        Args:
            schema_name (str): name of the postgresql schema
            table_name (str): name of the postgresq table
            custom_query (str): custom query to execute

        Returns:
            pd.DataFrame | bytes: Pandas DataFrame or bytes if file type not
                support.
        """

        data: pd.DataFrame | bytes = pd.read_sql_query(
            custom_query, self.connection
        )

        return data

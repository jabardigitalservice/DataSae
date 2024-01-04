#!/usr/bin/env python3

# Copyright (C) Free Software Foundation, Inc. All rights reserved.
# Licensed under the AGPL-3.0-only License. See LICENSE in the project root
# for license information.

"""local library."""

from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path

from pandas import DataFrame

from . import DataSource, FileType


@dataclass(repr=False)
class Local(DataSource):
    """
    Local.

    Represents a data source that connects to an local computer.
    """

    def __call__(
        self, file_path: str, **kwargs
    ) -> DataFrame | bytes:
        """
        __call__ method.

        Converts the data from the specified bucket and object name into a
        Pandas DataFrame.

        Args:
            file_path (str): The file path in the local computer.
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
        with open(file_path, 'rb') as response:
            data: DataFrame | bytes = super().__call__(
                FileType(Path(file_path).suffix),
                response.read(),
                **kwargs
            )

        return data

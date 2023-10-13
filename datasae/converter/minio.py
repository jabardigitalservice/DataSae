#!/usr/bin/env python3

# Copyright (c) Free Software Foundation, Inc. All rights reserved.
# Licensed under the AGPL-3.0-only License. See LICENSE in the project root
# for license information.

from dataclasses import dataclass

from . import DataSource


@dataclass(repr=False)
class Minio(DataSource):
    endpoint: str
    access_key: str
    secret_key: str

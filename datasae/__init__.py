#!/usr/bin/env python3

# Copyright (c) Free Software Foundation, Inc. All rights reserved.
# Licensed under the AGPL-3.0-only License. See LICENSE in the project root
# for license information.

"""
This is a standalone Python script that is used to execute a specific task.

Task:
- Generate a new version of the code snippet, with an additional docstring.
- Make sure the docstring starts and ends with standard Python docstring signs.
- The docstring should be in standard format. Use the 'Code Explanation' only
    as a reference, and don't copy its sections directly.
- Except for the docstring, the new code should be identical to the original
    code snippet. Keep existing code comments, line comments, blank lines,
    formatting, etc.
"""

# DataSource
from .converter.gsheet import GSheet
from .converter.s3 import S3
from .converter.sql import Sql
# DataType
from .boolean import Boolean
from .float import Float
from .integer import Integer
from .string import String
from .timestamp import Timestamp

# DataSource
GSheet
S3
Sql
# DataType
Boolean
Float
Integer
String
Timestamp

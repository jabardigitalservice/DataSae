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
try:
    from .converter.gsheet import GSheet

    GSheet
except ImportError:
    pass

try:
    from .converter.s3 import S3

    S3
except ImportError:
    pass

try:
    from .converter.sql import Sql

    Sql
except ImportError:
    pass


# DataType
try:
    from .boolean import Boolean

    Boolean
except ImportError:
    pass

try:
    from .float import Float

    Float
except ImportError:
    pass


try:
    from .integer import Integer

    Integer
except ImportError:
    pass

try:
    from .string import String

    String
except ImportError:
    pass

try:
    from .timestamp import Timestamp

    Timestamp
except ImportError:
    pass

<!--
Copyright (c) Free Software Foundation, Inc. All rights reserved.
Licensed under the AGPL-3.0-only License. See LICENSE in the project root for license information.
-->

# DataSae

[![Docs](https://img.shields.io/badge/Docs-blue)](https://jabardigitalservice.github.io/DataSae/)
[![License](https://img.shields.io/github/license/jabardigitalservice/DataSae?logoColor=black&label=License&labelColor=black&color=brightgreen)](https://github.com/jabardigitalservice/DataSae/blob/main/LICENSE)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/DataSae?logo=python&label=Python&labelColor=black)](https://pypi.org/project/DataSae/)
[![PyPI - Version](https://img.shields.io/pypi/v/DataSae?logo=pypi&label=PyPI&labelColor=black)](https://pypi.org/project/DataSae/)
[![GitHub Action](https://img.shields.io/github/actions/workflow/status/jabardigitalservice/DataSae/python.yaml?logo=GitHub&label=CI/CD&labelColor=black)](https://github.com/jabardigitalservice/DataSae/actions/workflows/python.yaml)
[![Coverage](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/jabardigitalservice/DataSae/python-coverage-comment-action-data/endpoint.json&labelColor=black)](https://htmlpreview.github.io/?https://github.com/jabardigitalservice/DataSae/blob/python-coverage-comment-action-data/htmlcov/index.html)

Data Quality Framework provides by Jabar Digital Service

## Converter

[https://github.com/jabardigitalservice/DataSae/blob/733d16fc8a39d25d56594de63c7ec4ad1fc0225c/tests/data/config.json#L1-L30](https://github.com/jabardigitalservice/DataSae/blob/733d16fc8a39d25d56594de63c7ec4ad1fc0225c/tests/data/config.json#L1-L30)

[https://github.com/jabardigitalservice/DataSae/blob/733d16fc8a39d25d56594de63c7ec4ad1fc0225c/tests/data/config.yaml#L1-L24](https://github.com/jabardigitalservice/DataSae/blob/733d16fc8a39d25d56594de63c7ec4ad1fc0225c/tests/data/config.yaml#L1-L24)

### Google Spreadsheet

[https://github.com/jabardigitalservice/DataSae/blob/4308324d066c6627936773ab2d5b990adaa60100/tests/data/creds.json#L1-L12](https://github.com/jabardigitalservice/DataSae/blob/4308324d066c6627936773ab2d5b990adaa60100/tests/data/creds.json#L1-L12)

```sh
pip install 'DataSae[converter,gsheet]'
```

```py
from datasae.converter import Config

# From JSON
config = Config('DataSae/tests/data/config.json')
gsheet = config('test_gsheet')
df = gsheet('Sheet1')
df = gsheet('Sheet1', 'gsheet_id')

# From YAML
config = Config('DataSae/tests/data/config.yaml')
gsheet = config('test_gsheet')
df = gsheet('Sheet1')
df = gsheet('Sheet1', 'gsheet_id')
```

### S3

```sh
pip install 'DataSae[converter,s3]'
```

```py
from datasae.converter import Config

# From JSON
config = Config('DataSae/tests/data/config.json')
s3 = config('test_s3')
df = s3('bucket_name', 'path/file_name.csv')
df = s3('bucket_name', 'path/file_name.json')
df = s3('bucket_name', 'path/file_name.parquet')
df = s3('bucket_name', 'path/file_name.xlsx', sheet_name='Sheet1')

# From YAML
config = Config('DataSae/tests/data/config.yaml')
s3 = config('test_s3')
df = s3('bucket_name', 'path/file_name.csv')
df = s3('bucket_name', 'path/file_name.json')
df = s3('bucket_name', 'path/file_name.parquet')
df = s3('bucket_name', 'path/file_name.xlsx', sheet_name='Sheet1')
```

### SQL

```sh
pip install 'DataSae[converter,sql]'
```

#### MariaDB or MySQL

```py
from datasae.converter import Config

# From JSON
config = Config('DataSae/tests/data/config.json')
mariadb_or_mysql = config('test_mariadb_or_mysql')
df = mariadb_or_mysql('select 1 column_name from schema_name.table_name;')
df = mariadb_or_mysql('path/file_name.sql')

# From YAML
config = Config('DataSae/tests/data/config.yaml')
mariadb_or_mysql = config('test_mariadb_or_mysql')
df = mariadb_or_mysql('select 1 column_name from schema_name.table_name;')
df = mariadb_or_mysql('path/file_name.sql')
```

#### PostgreSQL

```py
from datasae.converter import Config

# From JSON
config = Config('DataSae/tests/data/config.json')
postgresql = config('test_postgresql')
df = postgresql('select 1 column_name from schema_name.table_name;')
df = postgresql('path/file_name.sql')

# From YAML
config = Config('DataSae/tests/data/config.yaml')
postgresql = config('test_postgresql')
df = postgresql('select 1 column_name from schema_name.table_name;')
df = postgresql('path/file_name.sql')
```

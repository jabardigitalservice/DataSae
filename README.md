<!--
Copyright (C) Free Software Foundation, Inc. All rights reserved.
Licensed under the AGPL-3.0-only License. See LICENSE in the project root
for license information.
-->

# DataSae

[![Docs](https://img.shields.io/badge/Docs-blue)](https://jabardigitalservice.github.io/DataSae/)
[![License](https://img.shields.io/github/license/jabardigitalservice/DataSae?logoColor=black&label=License&labelColor=black&color=brightgreen)](https://github.com/jabardigitalservice/DataSae/blob/main/LICENSE)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/DataSae?logo=python&label=Python&labelColor=black)](https://pypi.org/project/DataSae/)
[![PyPI - Version](https://img.shields.io/pypi/v/DataSae?logo=pypi&label=PyPI&labelColor=black)](https://pypi.org/project/DataSae/)
[![GitHub Action](https://img.shields.io/github/actions/workflow/status/jabardigitalservice/DataSae/python_docker.yaml?logo=GitHub&label=CI/CD&labelColor=black)](https://github.com/jabardigitalservice/DataSae/actions/workflows/python_docker.yaml)
[![Coverage](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/jabardigitalservice/DataSae/python-coverage-comment-action-data/endpoint.json&labelColor=black)](https://htmlpreview.github.io/?https://github.com/jabardigitalservice/DataSae/blob/python-coverage-comment-action-data/htmlcov/index.html)

Data Quality Framework provides by Jabar Digital Service

- [Configuration Files](#configuration-files)
- [Checker for Data Quality](#checker-for-data-quality)
  - [Python Code](#python-code)
  - [Command Line Interface (CLI)](#command-line-interface-cli)
- [Converter from Any Data Source to Pandas's DataFrame](#converter-from-any-data-source-to-pandass-dataframe)
  - [Local Computer](#local-computer)
  - [Google Spreadsheet](#google-spreadsheet)
  - [S3](#s3)
  - [SQL](#sql)
    - [MariaDB or MySQL](#mariadb-or-mysql)
    - [PostgreSQL](#postgresql)

## Configuration Files

[https://github.com/jabardigitalservice/DataSae/blob/46ef80072b98ca949084b4e1ae50bcf23d07d646/tests/data/config.json#L1-L183](https://github.com/jabardigitalservice/DataSae/blob/46ef80072b98ca949084b4e1ae50bcf23d07d646/tests/data/config.json#L1-L183)

[https://github.com/jabardigitalservice/DataSae/blob/46ef80072b98ca949084b4e1ae50bcf23d07d646/tests/data/config.yaml#L1-L120](https://github.com/jabardigitalservice/DataSae/blob/46ef80072b98ca949084b4e1ae50bcf23d07d646/tests/data/config.yaml#L1-L120)

## Checker for Data Quality

> [!NOTE]  
> You can use [DataSae Column's Function Based on Data Type](functions.md) for adding column checker function data quality in the config file.

```sh
pip install 'DataSae[converter,gsheet,s3,sql]'
```

### Python Code

```py
from datasae.converter import Config

# From JSON
config = Config('DataSae/tests/data/config.json')

# From YAML
config = Config('DataSae/tests/data/config.yaml')

# Check all data qualities on configuration
config.checker  # dict result

# Check data quality by config name
config('test_local').checker  # list of dict result
config('test_gsheet').checker  # list of dict result
config('test_s3').checker  # list of dict result
config('test_mariadb_or_mysql').checker  # list of dict result
config('test_postgresql').checker  # list of dict result
```

Example results:
[https://github.com/jabardigitalservice/DataSae/blob/46ef80072b98ca949084b4e1ae50bcf23d07d646/tests/data/checker.json#L1-L432](https://github.com/jabardigitalservice/DataSae/blob/46ef80072b98ca949084b4e1ae50bcf23d07d646/tests/data/checker.json#L1-L432)

### Command Line Interface (CLI)

```sh
datasae --help
 
 Usage: datasae [OPTIONS] FILE_PATH
 
 Checker command.
 Creates checker result based on the configuration provided in the checker section of the data source's configuration file.
╭─ Arguments ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ *    file_path      TEXT  The source path of the .json or .yaml file [default: None] [required]                                    │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --config-name                       TEXT  If the config name is not set, it will create all of the checker results [default: None] │
│ --yaml-display    --json-display          [default: yaml-display]                                                                  │
│ --save-to-file-path                 TEXT  [default: None]                                                                          │
│ --help                                    Show this message and exit.                                                              │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

Example commands:

```sh
datasae DataSae/tests/data/config.yaml # Check all data qualities on configuration
datasae DataSae/tests/data/config.yaml --config-name test_local # Check data quality by config name
```

> [!TIP]
> Actually, we have example for DataSae implementation in Apache Airflow, but for now it is for private use only. Internal developer can see it at this [git repository](https://gitlab.com/jdsteam/core-data-platform/data-products/example-datasae-airflow).

## Converter from Any Data Source to Pandas's DataFrame

> [!NOTE]  
> Currently support to convert from CSV, JSON, Parquet, Excel, Google Spreadsheet, and SQL.

```sh
pip install 'DataSae[converter]'
```

### Local Computer

```py
from datasae.converter import Config

# From JSON
config = Config('DataSae/tests/data/config.json')

# From YAML
config = Config('DataSae/tests/data/config.yaml')

# Local computer file to DataFrame
local = config('test_local')

df = local('path/file_name.csv', sep=',')
df = local('path/file_name.json')
df = local('path/file_name.parquet')
df = local('path/file_name.xlsx', sheet_name='Sheet1')

df = local('path/file_name.csv')  # Default: sep = ','
df = local('path/file_name.json')
df = local('path/file_name.parquet')
df = local('path/file_name.xlsx')  # Default: sheet_name = 'Sheet1'
```

### Google Spreadsheet

[https://github.com/jabardigitalservice/DataSae/blob/4308324d066c6627936773ab2d5b990adaa60100/tests/data/creds.json#L1-L12](https://github.com/jabardigitalservice/DataSae/blob/4308324d066c6627936773ab2d5b990adaa60100/tests/data/creds.json#L1-L12)

```sh
pip install 'DataSae[converter,gsheet]'
```

```py
from datasae.converter import Config

# From JSON
config = Config('DataSae/tests/data/config.json')

# From YAML
config = Config('DataSae/tests/data/config.yaml')

# Google Spreadsheet to DataFrame
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

# From YAML
config = Config('DataSae/tests/data/config.yaml')

# S3 object to DataFrame
s3 = config('test_s3')

df = s3('path/file_name.csv', sep=',')
df = s3('path/file_name.json')
df = s3('path/file_name.parquet')
df = s3('path/file_name.xlsx', sheet_name='Sheet1')

df = s3('path/file_name.csv', 'bucket_name')  # Default: sep = ','
df = s3('path/file_name.json', 'bucket_name')
df = s3('path/file_name.parquet', 'bucket_name')
df = s3('path/file_name.xlsx', 'bucket_name')  # Default: sheet_name = 'Sheet1'
```

### SQL

```sh
pip install 'DataSae[converter,sql]'
```

> [!IMPORTANT]
> For MacOS users, if [pip install failed](https://stackoverflow.com/questions/67876857/mysqlclient-wont-install-via-pip-on-macbook-pro-m1-with-latest-version-of-big-s) at `mysqlclient`, please run this and retry to install again after that.
>
> ```sh
> brew install mysql
> ```

#### MariaDB or MySQL

```py
from datasae.converter import Config

# From JSON
config = Config('DataSae/tests/data/config.json')

# From YAML
config = Config('DataSae/tests/data/config.yaml')

# MariaDB or MySQL to DataFrame
mariadb_or_mysql = config('test_mariadb_or_mysql')
df = mariadb_or_mysql('select 1 column_name from schema_name.table_name;')
df = mariadb_or_mysql('path/file_name.sql')
```

#### PostgreSQL

```py
from datasae.converter import Config

# From JSON
config = Config('DataSae/tests/data/config.json')

# From YAML
config = Config('DataSae/tests/data/config.yaml')

# PostgreSQL to DataFrame
postgresql = config('test_postgresql')
df = postgresql('select 1 column_name from schema_name.table_name;')
df = postgresql('path/file_name.sql')
```

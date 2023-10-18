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

[https://github.com/jabardigitalservice/DataSae/blob/9ae19e7dc52b5cbed8bcd42559e8a78c3c64691a/tests/data/config.json#L1-L8](https://github.com/jabardigitalservice/DataSae/blob/9ae19e7dc52b5cbed8bcd42559e8a78c3c64691a/tests/data/config.json#L1-L8)

[https://github.com/jabardigitalservice/DataSae/blob/9ae19e7dc52b5cbed8bcd42559e8a78c3c64691a/tests/data/config.yaml#L1-L5](https://github.com/jabardigitalservice/DataSae/blob/9ae19e7dc52b5cbed8bcd42559e8a78c3c64691a/tests/data/config.yaml#L1-L5)

### MinIO

```sh
pip install 'DataSae[converter,minio]'
```

```py
from datasae.converter import Config

# From JSON
config_from_json = Config('DataSae/tests/data/config.json')
minio_from_json = config_from_json('test_minio')
df_csv_from_json = minio_from_json('bucket_name', 'path/file_name.csv')
df_json_from_json = minio_from_json('bucket_name', 'path/file_name.json')
df_parquet_from_json = minio_from_json('bucket_name', 'path/file_name.parquet')
df_xlsx_from_json = minio_from_json('bucket_name', 'path/file_name.xlsx', sheet_name='Sheet1')

# From YAML
config_from_yaml = Config('DataSae/tests/data/config.yaml')
minio_from_yaml = config_from_yaml('test_minio')
df_csv_from_yaml = minio_from_yaml('bucket_name', 'path/file_name.csv')
df_json_from_yaml = minio_from_yaml('bucket_name', 'path/file_name.json')
df_parquet_from_yaml = minio_from_yaml('bucket_name', 'path/file_name.parquet')
df_xlsx_from_yaml = minio_from_yaml('bucket_name', 'path/file_name.xlsx', sheet_name='Sheet1')
```

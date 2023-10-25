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

[https://github.com/jabardigitalservice/DataSae/blob/be7cb20fbd54293bae8a4949bf4bb6a1da1b87f6/tests/data/config.json#L1-L8](https://github.com/jabardigitalservice/DataSae/blob/be7cb20fbd54293bae8a4949bf4bb6a1da1b87f6/tests/data/config.json#L1-L8)

[https://github.com/jabardigitalservice/DataSae/blob/be7cb20fbd54293bae8a4949bf4bb6a1da1b87f6/tests/data/config.yaml#L1-L5](https://github.com/jabardigitalservice/DataSae/blob/be7cb20fbd54293bae8a4949bf4bb6a1da1b87f6/tests/data/config.yaml#L1-L5)

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

### Google Spreadsheet

```sh
pip install 'DataSae[converter,google-spreadsheet]'
```

```py
from datasae.converter import Config

# From JSON
config = Config('DataSae/tests/data/config.json')
spreadsheet = config('test_spreadsheet')
df = spreadsheet('google-spreadsheet-id','sheet_name')

# From YAML
config = Config('DataSae/tests/data/config.yaml')
spreadsheet = config('test_spreadsheet')
df = spreadsheet('google-spreadsheet-id','sheet_name')
```
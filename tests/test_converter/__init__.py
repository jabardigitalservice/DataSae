#!/usr/bin/env python3

# Copyright (c) Free Software Foundation, Inc. All rights reserved.
# Licensed under the AGPL-3.0-only License. See LICENSE in the project root
# for license information.

from datasae.converter import Config

CONFIG_JSON: Config = Config('tests/data/config.json')
CONFIG_YAML: Config = Config('tests/data/config.yaml')

#!/usr/bin/env python3

# Copyright (C) Free Software Foundation, Inc. All rights reserved.
# Licensed under the AGPL-3.0-only License. See LICENSE in the project root
# for license information.

"""
CLI.

This code snippet is a command-line interface (CLI) script using the Typer
library. It defines a command called "checker" that creates checker results
based on the configuration provided in a data source's configuration file.

The "checker" command takes the following arguments:
- file_path: The source path of the configuration file.
- config_name: Optional. The name of the specific configuration to use.
- yaml_display: Optional. A flag to determine whether to display the results
    in YAML format or JSON format.

The "checker" command uses the Config class from the "converter" module to
load the configuration file and retrieve the checker results. It then prints
the results using the rich library, either in YAML format or JSON format based
on the value of the yaml_display flag.

To use this script, run it from the command line and provide the necessary
arguments.

Example usage:
datasae data.json --yaml-display --config-name some_config_name
datasae data.yaml --json-display
"""

import json

from rich import print, print_json
from rich.syntax import Syntax
from typer import Argument, Option, Typer
from typing_extensions import Annotated
import yaml

from .converter import Config

cli: Typer = Typer(add_completion=False)


@cli.command()
def checker(
    file_path: Annotated[
        str,
        Argument(help='The source path of the .json or .yaml file')
    ],
    config_name: Annotated[
        str,
        Option(
            help='If the config name is not set, it will create all of the '
            'checker results'
        )
    ] = None,
    yaml_display: Annotated[
        bool,
        Option('--yaml-display/--json-display')
    ] = True,
    save_to_file_path: str = None
):
    """
    Checker command.

    Creates checker result based on the configuration provided in the checker
    section of the data source's configuration file.
    """
    config: Config = Config(file_path)
    result: list[dict] | dict = (
        config(config_name).checker
        if config_name else config.checker
    )

    if yaml_display:
        result: str = yaml.safe_dump(result)

        if save_to_file_path:
            with open(save_to_file_path, 'w') as output_file:
                output_file.write(result)
        else:
            print(Syntax(result, 'yaml'))
    else:
        if save_to_file_path:
            with open(save_to_file_path, 'w') as output_file:
                json.dump(result, output_file)
        else:
            print_json(data=result)


if __name__ == '__main__':
    cli()  # pragma: no cover

#!/usr/bin/env python3

# Copyright (C) Free Software Foundation, Inc. All rights reserved.
# Licensed under the AGPL-3.0-only License. See LICENSE in the project root
# for license information.

"""Tests library."""

from unittest import TestCase

from typer.testing import CliRunner

from datasae.__main__ import cli

MESSAGE: str = 'Result Not Match'


class TestMain(TestCase):
    """TestMain class."""

    def test_cli(self):
        """test_cli method."""
        cli_runner: CliRunner = CliRunner()
        command: list = [
            '--config-name',
            'test_local',
            'tests/data/config.yaml',
        ]

        # Yaml Display
        self.assertEqual(
            cli_runner.invoke(cli, command).exit_code,
            0
        )
        self.assertEqual(
            cli_runner.invoke(
                cli,
                [
                    '--save-to-file-path',
                    '/tmp/output',
                    *command
                ]
            ).exit_code,
            0
        )

        # Json Display
        self.assertEqual(
            cli_runner.invoke(
                cli,
                [
                    '--json-display',
                    *command
                ]
            ).exit_code,
            0
        )
        self.assertEqual(
            cli_runner.invoke(
                cli,
                [
                    '--json-display',
                    '--save-to-file-path',
                    '/tmp/output',
                    *command
                ]
            ).exit_code,
            0
        )

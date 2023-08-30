#!/usr/bin/env python3

# This module is part of DataSae and is released under
# the AGPL-3.0-only License: https://opensource.org/license/agpl-v3/

import unittest

from datasae.example import add_one


class ExampleTestCase(unittest.TestCase):
    def test_add_one(self):
        self.assertEqual(add_one(1), 2)

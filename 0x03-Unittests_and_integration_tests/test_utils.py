#!/usr/bin/python3
"""Parameterize a unit test"""
import unittest
from utils import access_nested_map
from parameterized import parameterized
from typing import (
        Mapping,
        Sequence
        )


class TestAccessNestedMap(unittest.TestCase):
    """Base TestCase"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_acces_nested_map(self, nested_map, path, expected):
        """tests data from access_nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)


if __name__ == "__main__":
    unittest.main()        

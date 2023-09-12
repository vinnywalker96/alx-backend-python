#!/usr/bin/env python3
"""Parameterize a unit test"""
import unittest
from utils import (
        access_nested_map,
        get_json
        )
from unittest.mock import patch, Mock
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
    def test_access_nested_map(self, nested_map, path, expected):
        """tests data from access_nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), None),
        ({"a": 1}, ("a", "b"), None),
        ])
    def test_access_nested_map_exception(
            self, nested_map, path, expected):
        """ test"""
        with self.assertRaises(KeyError):
            self.assertEqual(
                    access_nested_map(
                        nested_map, path), expected)


class TestGetJson(unittest.TestCase):
    """Moct HTTP calls class"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
        ])
    def test_get_json(self, test_url, test_payload):
        """Test Url"""
        args = {'json.return_value': test_payload}
        with patch("requests.get", return_value=Mock(**args)) as req:
            self.assertEqual(get_json(test_url), test_payload)
            req.assert_called_once_with(test_url)


if __name__ == "__main__":
    unittest.main()

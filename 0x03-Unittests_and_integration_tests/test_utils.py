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
    @patch("requests.get")
    def test_get_json(self, mock_get):
        """Test requests"""
        mock_get.return_value.json.return_value = {"payload": True}
        result = get_json("http://example.com")
        self.assertEqual(result, {"payload": True})
        mock_get.assert_called_once("http://example.com")

if __name__ == "__main__":
    unittest.main() 

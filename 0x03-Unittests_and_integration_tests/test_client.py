#!/usr/bin/env python3
"""Parameterize and patch as decorators"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock, MagicMock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Base Test org class"""
    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"})
        ])
    @patch("client.get_json")
    def test_org(self, org, response, mock_data):
        """Testing org
        Args:
            org:
            response
            mock_data
        """
        mock_data.return_value = MagicMock(return_value=response)
        org_client = GithubOrgClient(org)
        self.assertEqual(org_client.org(), response)
        mock_data.assert_called_once_with(
                f"https://api.github.com/orgs/{org}")


if __name__ == "__main__":
    unittest.main()

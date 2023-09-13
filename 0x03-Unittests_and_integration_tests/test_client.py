#!/usr/bin/env python3
"""Parameterize and patch as decorators"""
import unittest
from parameterized import parameterized
from unittest.mock import (
        patch,
        Mock,
        MagicMock,
        PropertyMock
        )
from client import GithubOrgClient
from typing import Dict


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

    def test_public_repos_url(self) -> None:
        """Tests the `_public_repos_url` property."""
        with patch(
                "client.GithubOrgClient.org",
                new_callable=PropertyMock,
                ) as mock_org:
            mock_org.return_value = {
                'repos_url': "https://api.github.com/users/google/repos",
            }
            self.assertEqual(
                GithubOrgClient("google")._public_repos_url,
                "https://api.github.com/users/google/repos",
            )


if __name__ == "__main__":
    unittest.main()

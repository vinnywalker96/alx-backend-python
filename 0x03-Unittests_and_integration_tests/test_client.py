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
                GithubOrgClient("google").public_repos_url,
                "https://api.github.com/users/google/repos",
            )

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json: MagicMock) -> None:
        """Tests the `public_repos` method."""
        test_payload = {
                'repos_url': 'https://api.github.com/orgs/google/repos',
                'repos': [
                    {
                        "id": 23455,
                        "name": "test",
                        "private": False,
                        "owner": "Google"
                    }
                ]
                
               }
        mock_get_json.return_value = test_payload[
            "repos"
            ]
        with patch(
                "client.GithubOrgClient._public_repos_url",
                new_callable=PropertyMock,
        ) as mock_public_repos_url:
            mock_public_repos_url.return_value = test_payload["repos_url"]
            self.assertEqual(
                GithubOrgClient("google").public_repos(),
                [
                    "users",
                    "likes",
                ],
            )
            mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once()

    @parameterized.expand([
        ({'license': {'key': "bsd-3-clause"}}, "bsd-3-clause", True),
        ({'license': {'key': "bsl-1.0"}}, "bsd-3-clause", False),
    ])
    def test_has_license(self, repo: Dict, key: str, expected: bool):
        """Test if repo has licence"""
        org_client = GithubOrgClient("google")
        has_licence = org_client.has_license(repo, key)
        self.assertEqual(has_licence, expected)


if __name__ == "__main__":
    unittest.main()

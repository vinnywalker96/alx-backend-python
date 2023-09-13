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

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json: MagicMock) -> None:
        """Tests the `public_repos` method."""
        test_payload = {
                'repos_url': 'https://api.github.com/orgs/google/repos', 
	            'repo': [
                    {
                        'login': 'google',
	                    'id': 1342004,

	                },
                    {
                        'node_id': 'MDEyOk9yZ2FuaXphdGlvbjEzNDIwMDQ=',
                        'url': 'https://api.github.com/orgs/google',
                        'repos_url': 'https://api.github.com/orgs/google/repos',
                        'events_url': 'https://api.github.com/orgs/google/events',
                        'hooks_url': 'https://api.github.com/orgs/google/hooks', 
                        'issues_url': 'https://api.github.com/orgs/google/issues',
                        'members_url': 'https://api.github.com/orgs/google/members{/member}',
                    },
                    {
                        'name': 'Google',
                        'company': None, 
                        'blog': 'https://opensource.google/',
                        'location': None, 
                        'email': 'opensource@google.com', 
                        'twitter_username': 'GoogleOSS', 
                        'is_verified': True,
                        'has_organization_projects': True, 
                        'has_repository_projects': True, 
                        'public_repos': 2552, 
                        'public_gists': 0, 
                        'followers': 28884,
                        'following': 0, 
                        'html_url': 'https://github.com/google', 
                        'created_at': '2012-01-18T01:30:18Z', 
                        'updated_at': '2021-12-30T01:40:20Z', 
                        'archived_at': None, 'type': 'Organization'
                    },
                    ]
                }
        mock_get_json.return_value = test_payload["repo"]
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







if __name__ == "__main__":
    unittest.main()

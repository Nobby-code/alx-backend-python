#!/usr/bin/env python3
"""Unit tests for GithubOrgClient"""

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Tests for GithubOrgClient.org"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value """

        # Setup expected response and mock
        expected_result = {"login": org_name}
        mock_get_json.return_value = expected_result

        # Instantiate the client and call org
        client = GithubOrgClient(org_name)
        result = client.org

        # Assertions
        self.assertEqual(result, expected_result)
        url_org = "https://api.github.com/orgs/"
        mock_get_json.assert_called_once_with(f"{url_org}{org_name}")

    def test_public_repos_url(self):
        """Test that _public_repos_url returns expected value from mocked org
        """
        test_url = "https://api.github.com/orgs/test-org/repos"
        with patch.object(
            GithubOrgClient,
            "org",
            new_callable=PropertyMock
        ) as mock_org:
            mock_org.return_value = {"repos_url": test_url}
            client = GithubOrgClient("test-org")

            self.assertEqual(client._public_repos_url, test_url)
            mock_org.assert_called_once()

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """Test GithubOrgClient.public_repos returns expected repo list"""

        # Sample payload returned by get_json (repos payload)
        repos_payload = [
            {"name": "rep1"},
            {"name": "repo2"},
            {"name": "repo3"},
        ]
        mock_get_json.return_value = repos_payload

        # Patch the _public_repos_url property to return a dummy URL
        with patch.object(
            GithubOrgClient,
            "_public_repos_url",
            new_callable=PropertyMock
        ) as mock_public_repos_url:
            mock_public_repos_url.return_value = "http://fake.url"

            client = GithubOrgClient("testorg")
            result = client.public_repos()

            # Assertions
            self.assertEqual(result, ["repo1", "repo2", "repo3"])
            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with("http://fake.url")


if __name__ == '__main__':
    unittest.main()

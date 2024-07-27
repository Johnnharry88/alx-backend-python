#!/usr/bin/env python3
""" Moudle used for test"""

from typing import Dict
from parameterized import parameterized
from unittest import TestCase, mock
from unittest.mock import patch, Mock, MagicMock
from unittest.mock import PropertyMock
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(TestCase):
    """ Class used for testing out GithubOrgClient"""
    @parameterized.expand([
        ('google', {'login': 'google'}),
        ('abc', {'login': 'abc'}),
    ])
    @patch('client.get_json')
    def test_org(self, org: str, exp_response: Dict,
                 m_json: MagicMock) -> None:
        """ Tests out the org method correct output"""
        gx = GithubOrgClient(org)
        self.assertEqual(gx.org(), exp_response)
        m_json.assert_called_once_with(
            f"https://api.github.com/orgs/{name_org}"
            )

    def test_public_repos_url(self) -> None:
        """ Tests out the public repo property"""
        with patch('client.GithubOrgClient.org',
             new_callable=PropertyMock) as _mock:
            _mock.return_value = {
                    'repos_url': 'https://api.github.com/users/google/repos',
            }
            self.assertEqual(
                GithubOrgClient('google')._public_repos_url,
                'https://api.github.com/users/google/repos',
            )

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json: MagicMock) -> None:
        """ Tests out method for the public repos"""
        test_payload = {
            'repos_url': "https://api.github.com/users/google/repos",
            'repos': [
                {
                    "id": 7697149,
                    "name": "episodes.dart",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/episodes.dart",
                    "created_at": "2013-01-19T00:31:37Z",
                    "updated_at": "2019-09-23T11:53:58Z",
                    "has_issues": True,
                    "forks": 22,
                    "default_branch": "master",
                },
                {
                    "id": 8566972,
                    "name": "kratu",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/kratu",
                    "created_at": "2013-03-04T22:52:33Z",
                    "updated_at": "2019-11-15T22:22:16Z",
                    "has_issues": True,
                    "forks": 32,
                    "default_branch": "master",
                },
            ]
        }
        mock_get_json.return_value = test_payload['repos']
        with patch(
                'client.GithubOrgClient._public_repos_url',
                new_callable=PropertyMock,
                ) as mock_pub_repo:
            mock_pub_repo.return_value = test_payload['repos_url']
            self.assertEqual(
                GithubOrgClient('google').public_repos(),
                [
                    'episodes.dart',
                    'kratu',
                ],
            )
            mock_pub_repo.assert_called_once()
        mock_get_json.assert_called_once()

    @parameterized.expand([
        ({'license': {'key': 'bsd-3-clause'}}, 'bsd-3-clause', True),
        ({'license': {'key': 'bs1-1.0'}}, 'bsd-3-clause', False),
    ])
    def test_has_license(self, repo: Dict, key: str, expected: bool) -> None:
        """Tests to check for has license method"""
        gx = GithubOrgClient('google')
        pos_license = gx.has_license(repo, key)
        self.assertEqual(pos_license, expected)

#!/usr/bin/env python3
""" Moudle used for test"""

from typing import Dict
from parameterized import parameterized, parameterized_class
from unittest import TestCase, mock
from unittest.mock import (
    patch,
    Mock,
    MagicMock,
    PropertyMock
)
from client import (
    GithubOrgClient\
)
from fixtures import TEST_PAYLOAD
from requests import HTTPError


class TestGithubOrgClient(TestCase):
    """ Class used for testing out GithubOrgClient"""
    @parameterized.expand([
        ('google', {'login': 'google'}),
        ('abc', {'login': 'abc'}),
    ])
    @patch(
        'client.get_json'
    )
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


@parameterized_class([
    {
        'org_payload': TEST_PAYLOAD[0][0],
        'repos_payload': TEST_PAYLOAD[0][1],
        'expected_repos': TEST_PAYLOAD[0][2],
        'apache2_repos': TEST_PAYLOAD[0][3],
    },
])
class TestIntegrationGithubOrgClient(TestCase):
    """class that runs integration tests for GithubOrgClient
    class"""
    @classmethod
    def setUpClass(cls) -> None:
        """ Sets class features prior to tunning test"""
        route_payload = {
            'https://api.github.com/orgs/google': cls.org_payload,
            'https://api.github.com/orgs.google/repos': cls.repos_payload,
        }

        def get_payload(url):
            if url in route_payload:
                return Mock(**{'json.return_value': route_payload[url]})
            return HTTPError
        cls.get_patcher = patch('requests.get', side_effect=get_payload)
        cls.get_patcher.start()

    def test_public_repos(self) -> None:
        """Test the public repos method"""
        self.assertEqual(
            GithubOrgClient('google').public_repos(),
            self.expeted_repos,
        )

    def test_public_repo_with_license(self) -> None:
        """Test the public_repo methodw with a license"""
        self.assertEqual(
            GithubOrgClient('google').public_repos(license='apache-2.0'),
            self.apache2_repos,
        )

    @classmethod
    def tearDownClass(cls) -> None:
        """Removes clas after testing"""
        cls.get_patcher.stop()

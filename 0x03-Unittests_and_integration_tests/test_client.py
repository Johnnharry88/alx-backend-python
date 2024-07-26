#!/usr/bin/env python3
""" Moudle used for test"""

from parameterized import parameterized
from unittest import TestCase, mock
from unittest.mock import patch, Mock
from client import GithubOrgClient


class TestGithubOrgClient(TestCase):
    """ Class used for testing out GithubOrgClient"""
    @parameterized.expand([
        ('google'),
        ('abc'),
    ])
    @patch('client.get_json')
    def test_org(self, name_org, m_json):
        """ Tests for correct output"""
        gx = GithubOrgClient(name_org)
        gx.org()
        m_json.assert_called_once_with(
            f"https://api.github.com/orgs/{name_org}"
            )

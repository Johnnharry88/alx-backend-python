#!/usr/bin/env python3
"""Unittest and Integration Module"""

from unittest import TestCase, mock
from unittest.mock import patch, Mock
from parameterized import parameterized

from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(TestCase):
    """Class used for testing Nested Map function"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, map, path, expected_output):
        """ Text method to ensure correct output """
        res_output = access_nested_map(map, path)
        self.assertEqual(res_output, expected_output)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b")
    ])
    def test_access_nested_map_exception(self, map, path, w_output):
        """Test out correct exception"""
        with self.assertRaises(KeyError) as x:
            access_nested_map(map, path)
            self.assertEqual(w_output, x.exception)


class TestGetJson(TestCase):
    """ Class used for testing get jsoen function"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """Checks that the method returns correct output"""
        m_response = Mock()
        m_response.json.return_value = test_payload
        with patch("requests.get", return_value=m_response):
            check_response = get_json(test_url)
            self.assertEqual(test_payload, check_response)
            m_response.json.assert_called_once()


class TestMemoize(TestCase):
    """Class for testing memoize"""
    def test_memoize(self):
        """tests Function memoize"""
        class TestClass:
            """Class for testing"""

            def a_method(self):
                """Returns 42"""
                return 42

            @memoize
            def a_property(self):
                """Return property"""
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as patched:
            testout = TestClass()
            exp_return = testout.a_property

            self.assertEqual(exp_return, 42)
            patched.assert_called_once()

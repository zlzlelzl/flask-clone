from unittest import TestCase
import pytest
import unittest
# from db import db_connect, db_test


class TestDb:
    def test_db_connect():
        assert 1 == 1


class TestMainDev:
    pass


class TestMain:
    pass


class MyTests(TestCase):
    def test_one_plus_two(self):
        self.assertEqual(1 + 2, 3)

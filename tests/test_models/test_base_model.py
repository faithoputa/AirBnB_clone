#!/usr/bin/python3
"""Test BaseModel for expected behavior and documentation"""
import inspect
import json
import models
import pep8 as pycodestyle
import time
import unittest
from unittest.case import SkipTest
from unittest.mock import patch
from models.base_model import BaseModel


class TestBaseModelDocs(unittest.TestCase):
    """Tests to check the documentation of BaseModel class"""

    @classmethod
    def setUpClass(cls):
        """Set up for docstring tests"""
        cls.base_funcs = inspect.getmembers(BaseModel, inspect.isfunction)

    def test_pep8_conformance(self):
        """Test that models/base_model.py conforms to PEP8."""
        for path in ['models/base_model.py',
                     'tests/test_models/test_base_model.py']:
            with self.subTest(path=path):
                errors = pycodestyle.Checker(path).check_all()
                self.assertEqual(errors,   


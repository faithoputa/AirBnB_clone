#!/usr/bin/python3
""" Module for Test cases for the base model """
import datetime
import io
import sys
import unittest
from models.base_model import BaseModel


class Test_Base_model_class(unittest.TestCase):
    """ Class for Test Base model """

    def test_func(self):
        """ function for testing str, save, to_dict"""
        test_model = BaseModel()

        test_model.name = "first_test_model"
        test_model.my_number = 97

        s = str(test_model)
        self.assertIn("[BaseModel]", s)
        self.assertIn(test_model.id, s)
        self.assertIn(str(test_model.__dict__), s)

        test_model.save()

        s = str(test_model)
        self.assertIn("[BaseModel]", s)
        self.assertIn(test_model.id, s)
        self.assertIn(str(test_model.__dict__), s)

        d = test_model.to_dict()

        self.assertIsInstance(d, dict)

        self.assertIn("id", d)
        self.assertIn("created_at", d)
        self.assertIn("updated_at", d)
        self.assertIn("name", d)
        self.assertIn("my_number", d)
        self.assertIn("__class__", d)

    def test_04_baseModel(self):
        """ test attributes of basemodel after creation """

        test_model = BaseModel()
        test_model_json = test_model.to_dict()
        test_new_model = BaseModel(**test_model_json)

        self.assertIsNotNone(test_new_model.id)
        self.assertIsInstance(test_new_model.created_at, datetime.datetime)
        self.assertIsInstance(test_new_model.updated_at, datetime.datetime)

#!/usr/bin/python3
""" module for testing the city class"""
from models.city import City
import unittest


class test_city(unittest.TestCase):
    """ class to test for the city """

    def test_city_class(self):
        """ test the city """
        city_class_obj = City()

        self.assertEqual(city_class_obj.name, "")
        self.assertEqual(city_class_obj.state_id, "")

        string_form = str(city_class_obj)
        self.assertIn("[City]", string_form)
        self.assertIn(city_class_obj.id, string_form)
        self.assertIn(str(city_class_obj.__dict__), string_form)

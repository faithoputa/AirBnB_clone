#!/usr/bin/python3
""" Module to test module for class amenity"""
from models.amenity import Amenity
import unittest


class test_amenity(unittest.TestCase):
    """ test class for the amenity """

    def test_amenity_module(self):
        """ test module for the class amenity """
        amenity_class_obj = Amenity()

        self.assertEqual(amenity_class_obj.name, "")

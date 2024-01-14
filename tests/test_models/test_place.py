#!/usr/bin/python3
"""
Contains the TestPlaceDocs classes
"""

from datetime import datetime
import inspect
import models
from models.place import Place
from models.base_model import BaseModel
import pep8
import unittest


class TestPlaceDocs(unittest.TestCase):
    """Tests to check the documentation and style of Place class"""

    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.place_f = inspect.getmembers(Place, inspect.isfunction)

    def test_pep8_conformance_place(self):
        """Test that models/place.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/place.py'])
        self.assertEqual(
            result.total_errors, 0,
            "Found code style errors (and warnings)."
        )

    def test_pep8_conformance_test_place(self):
        """Test that tests/test_models/test_place.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_place.py'])
        self.assertEqual(
            result.total_errors, 0,
            "Found code style errors (and warnings)."
        )

    def test_place_module_docstring(self):
        """Test for the place.py module docstring"""
        self.assertIsNot(place.__doc__, None, "place.py needs a docstring")
        self.assertTrue(
            len(place.__doc__) >= 1,
            "place.py needs a docstring"
        )

    def test_place_class_docstring(self):
        """Test for the Place class docstring"""
        self.assertIsNot(
            Place.__doc__, None,
            "Place class needs a docstring"
        )
        self.assertTrue(
            len(Place.__doc__) >= 1,
            "Place class needs a docstring"
        )

    def test_place_func_docstrings(self):
        """Test for the presence of docstrings in Place methods"""
        for func in self.place_f:
            self.assertIsNot(
                func[1].__doc__, None,
                "{:s} method needs a docstring".format(func[0])
            )
            self.assertTrue(
                len(func[1].__doc__) >= 1,
                "{:s} method needs a docstring".format(func[0])
            )


class TestPlace(unittest.TestCase):
    """Test the Place class"""

    def setUp(self):
        """Set up a new Place instance for each test"""
        self.place = Place()

    def tearDown(self):
        """Clean up after each test"""
        del self.place

    def test_is_subclass(self):
        """Test that Place is a subclass of BaseModel"""
        self.assertIsInstance(self.place, BaseModel)
        self.assertTrue(hasattr(self.place, "id"))
        self.assertTrue(hasattr(self.place, "created_at"))
        self.assertTrue(hasattr(self.place, "updated_at"))

    def test_attributes_defaults(self):
        """Test Place attributes have default values"""
        attributes = [
            "city_id", "user_id", "name", "description",
            "number_rooms", "number_bathrooms", "max_guest",
            "price_by_night", "latitude", "longitude"
        ]
        for attr_name in attributes:
            self.assertTrue(hasattr(self.place, attr_name))
            attr_value = getattr(self.place, attr_name)
            if models.storage_t == 'db':
                self.assertEqual(attr_value, None)
            else:
                if type(attr_value) is str:
                    self.assertEqual(attr_value, "")
                elif type(attr_value) is int:
                    self.assertEqual(attr_value, 0)
                elif type(attr_value) is float:
                    self.assertEqual(attr_value, 0.0)

    def test_to_dict_creates_dict(self):
        """Test to_dict method creates a dictionary with proper attrs"""
        new_d = self.place.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertNotIn("_sa_instance_state", new_d)
        for attr in self.place.__dict__:
            if attr is not "_sa_instance_state":
                self.assertIn(attr, new_d)
        self.assertIn("__class__", new_d)

    def test_to_dict_values(self):
        """Test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        new_d = self.place.to_dict()
        self.assertEqual(new_d["__class__"], "Place")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated  


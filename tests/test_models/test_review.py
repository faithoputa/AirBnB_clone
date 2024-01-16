#!/usr/bin/python3
""" module for testing the review class"""
from models.review import Review
import unittest


class test_review(unittest.TestCase):
    """ class to test for the review class """

    def test_review_class(self):
        """ method to test the review module """
        review_class_obj = Review()

        self.assertEqual(review_class_obj.place_id, "")
        self.assertEqual(review_class_obj.user_id, "")
        self.assertEqual(review_class_obj.text, "")

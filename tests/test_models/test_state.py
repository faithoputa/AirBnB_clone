#!/usr/bin/python3
""" Module for Testing the state class """
from models.state import State
import unittest


class test_state(unittest.TestCase):
    """ test class case for class state """

    def test_case_state(self):
        """ method to test the state class """
        state_instance = State()

        self.assertEqual(state_instance.name, "")

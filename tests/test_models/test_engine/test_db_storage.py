#!/usr/bin/python3
"""Test for DBStorage class"""

import inspect
import json
import os
import unittest
from models.engine import db_storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
  


from unittest import TestCase
from unittest.mock import patch
import os
import db
from db import Db, Database
import ui
from menu import Menu

class TestDatabase(TestCase):
    
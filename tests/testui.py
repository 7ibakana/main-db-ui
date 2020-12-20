from unittest import TestCase
from unittest.mock import patch
import os
import db
from db import Db, Database
import ui
from menu import Menu

class TestUI(TestCase):
    @patch('builtins.print')
    def test_message(self, mock_print):
        ui.message('hey')
        mock_print.assert_called_with('hey')

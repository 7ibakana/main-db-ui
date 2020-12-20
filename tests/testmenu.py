from unittest import TestCase
from menu import Menu

class TestMenu(TestCase):
    def setUp(self):
        self.menu = Menu()
        def a():
            pass
        def b():
            pass
        self.a = a
        self.b = b
        self.menu.add_option('a', 'aaa', a)
        self.menu.add_option('b', 'bbb', b)

    def test_add_option(self):
        self.assertDictEqual({'a': 'aaa', 'b': 'bbb'}, self.menu.text_descriptions)
        self.assertDictEqual({'a': self.a, 'b': self.b}, self.menu.functions)
    
    def test_str(self):
        menu_string = 'a: aaa\nb: bbb'
        self.assertEqual(menu_string, str(self.menu))
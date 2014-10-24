import bar, baz
import unittest

class TestBar(unittest.TestCase):
    def setUp(self):
        self.items = range(5)
        self.mybar = bar.Bar(self.items)
    def test_bar_list_length(self):
        self.assertEqual(len(self.mybar.items), len(self.items)-2)
    def test_bar_sum(self):
        self.assertEqual(self.mybar.sum(), 6)

class TestBaz(unittest.TestCase):
    def setUp(self):
        self.items = range(5)
        self.baz = baz.Baz(self.items)
    def test_baz_constructor(self):
        #self.assertRaises(Exception, baz.Baz, list("abcdef"))
        self.assertRaises(baz.NotAnIntegerListException, baz.Baz, list("abcdef"))

 

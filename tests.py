import unittest
from functions import additions,append
class TestAddition(unittest.TestCase):

    def test_integer_to_integer(self):
        self.assertEqual(additions(1,10), 11)
    def test_integer_to_float(self):
        self.assertEqual(additions(1,10.5), 11.5)
    def test_integer_to_char(self):
        self.assertEqual(additions(1,'c'), 'FAIL')
    def test_integer_to_str(self):
        self.assertEqual(additions(1,"immposible"), 'FAIL')
    def test_integer_to_set(self):
        self.assertEqual(additions(1,{4,5,2}), 'FAIL')
    def test_integer_to_dict(self):
        self.assertEqual(additions(1,{"key":"value"}), 'FAIL')

class TestAppend(unittest.TestCase):
    def test_append(self):
        self.assertEqual(append([1,2,3],[4,'text',10.9524]),[1,2,3,4,'text',10.9524])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(AttributeError):
            append([1,2,3],[4,'text',10.9524])


class TestString(unittest.TestCase):
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

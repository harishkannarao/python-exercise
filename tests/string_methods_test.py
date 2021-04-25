import unittest
from assertpy import assert_that


# noinspection PyMethodMayBeStatic
class StringMethodsTest(unittest.TestCase):

    def test_upper(self):
        assert_that('foo'.upper()).is_equal_to('FOO')

    def test_isupper(self):
        assert_that('FOO'.isupper()).is_true()
        assert_that('foo'.isupper()).is_false()

    def test_split(self):
        s = 'hello world'
        assert_that(s.split()).is_equal_to(['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

import unittest
from isogram import is_isogram

class Test(unittest.TestCase):
    def test_isogram_true(self):
        self.assertTrue(is_isogram("abcde"))
        self.assertTrue(is_isogram(''))

    def test_isogram_false(self):
        self.assertFalse(is_isogram("abcdeaa"))
        self.assertFalse(is_isogram("abcdeaB"))

    def test_isogram_equals(self):
        self.assertEquals(is_isogram('Dermatoglyphics'), True)
        self.assertEquals(is_isogram('isogram'), True)
        self.assertEquals(is_isogram('thumbscrewjapingly'), True)
        self.assertEquals(is_isogram('moose'), False)
        self.assertEquals(is_isogram('abcdefghijklmnopqrstuwwxyz'), False)


if __name__ == '__main__':
    unittest.main()        
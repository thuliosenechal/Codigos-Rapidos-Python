import unittest
from letras_duplicadas import duplicate_count

class Test(unittest.TestCase):
    def test_string(self):
        self.assertEqual(duplicate_count(""), 0)
        self.assertEqual(duplicate_count("abcde"), 0)
        self.assertEqual(duplicate_count("abcdeaa"), 1)
        self.assertEqual(duplicate_count("abcdeaB"), 2)
        self.assertEqual(duplicate_count("Indivisibilities"), 2)

        lowercase,uppercase = 'abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        self.assertEqual(duplicate_count(lowercase), 0)
        self.assertEqual(duplicate_count(lowercase + "aaAb"), 2)

        self.assertEqual(duplicate_count(lowercase+lowercase), 26)
        self.assertEqual(duplicate_count(lowercase+uppercase), 26)

if __name__ == '__main__':
    unittest.main()        
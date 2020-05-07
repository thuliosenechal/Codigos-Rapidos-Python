import unittest
from formatar_string import namelist

class Test(unittest.TestCase):

    def test_case(self):
        self.assertEquals(namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}]), 'Bart, Lisa, Maggie, Homer & Marge')
        self.assertEquals(namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'}]), 'Bart, Lisa & Maggie')
        self.assertEquals(namelist([{'name': 'Bart'},{'name': 'Lisa'}]), 'Bart & Lisa')
        self.assertEquals(namelist([{'name': 'Bart'}]), 'Bart')
        self.assertEquals(namelist([]), '')

if __name__ == '__main__':
    unittest.main()        
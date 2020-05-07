import unittest
from criptografia import criptografia
from descriptografia import descriptografia


class Test(unittest.TestCase):

    def test_criptografia(self):
        self.assertEquals(criptografia('teste criptografia.'),
                                       'fqefq odubfasdmrum.')

    def test_descriptografia(self):
        self.assertEquals(descriptografia('fqefq odubfasdmrum.'),
                                          'teste criptografia.')

if __name__ == '__main__':
    unittest.main()
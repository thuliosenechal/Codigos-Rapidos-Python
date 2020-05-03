import unittest
from proximo_maior_numero import next_bigger

class Test(unittest.TestCase):

    def test_case(self):
        self.assertEquals(next_bigger(12),21)
        self.assertEquals(next_bigger(513),531)
        self.assertEquals(next_bigger(2017),2071)
        self.assertEquals(next_bigger(414),441)
        self.assertEquals(next_bigger(144),414)

if __name__ == '__main__':
    unittest.main()        
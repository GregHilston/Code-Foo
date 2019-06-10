import unittest
from solution import TwoCityScheduling

class TwoCitySchedulingTests(unittest.TestCase):
    def setUp(self):
        self.sut = TwoCityScheduling()

    def test1(self):
        self.assertEqual(110, self.sut.solve([[10, 20], [30, 200], [400, 50], [30, 20]]))

if __name__ == '__main__':
    unittest.main()
import unittest
from solution import RottingOranges

class RottingOrangesTests(unittest.TestCase):
    def setUp(self):
        self.sut = RottingOranges()

    def test_1(self):
        self.assertEqual(4, self.sut.solve(
            [
                [2,1,1],
                [1,1,0],
                [0,1,1]
            ]))

    def test_2(self):
        self.assertEqual(-1, self.sut.solve(
            [
                [2,1,1],
                [0,1,1],
                [1,0,1]
            ]))

    def test_3(self):
        self.assertEqual(0, self.sut.solve(
            [
                [0, 2]
            ]))

if __name__ == '__main__':
    unittest.main()
import unittest
from solution import NimGame

class NimGameTests(unittest.TestCase):
    def setUp(self):
        self.sut = NimGame()

    def test_1(self):
        self.assertEqual(True, self.sut.solve(1))

    def test_2(self):
        self.assertEqual(True, self.sut.solve(2))

    def test_3(self):
        self.assertEqual(True, self.sut.solve(3))

    def test_4(self):
        self.assertEqual(False, self.sut.solve(4))

    def test_5(self):
        self.assertEqual(True, self.sut.solve(5))

    def test_6(self):
        self.assertEqual(True, self.sut.solve(6))

    def test_7(self):
        self.assertEqual(True, self.sut.solve(7))

    def test_8(self):
        self.assertEqual(False, self.sut.solve(8))

    def test_9(self):
        self.assertEqual(True, self.sut.solve(9))

    def test_10(self):
        self.assertEqual(True, self.sut.solve(10))

    def test_11(self):
        self.assertEqual(True, self.sut.solve(11))

    def test_12(self):
        self.assertEqual(False, self.sut.solve(12))

    def test_13(self):
        self.assertEqual(True, self.sut.solve(13))
if __name__ == '__main__':
    unittest.main()
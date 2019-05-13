import unittest
from solution import Bowling

class BowlingTests(unittest.TestCase):
    def setUp(self):
        self.sut = Bowling()

    def test_easy(self):
        self.assertEqual(100, self.sut.solve("55 55 55 55 55 55 55 55 55 55"))

    # def test_all_strikes(self):
    #     self.assertEqual(300, self.sut.solve("X X X X X X X X X X X X"))

    # def test_all_nines_and_misses(self):
    #     self.assertEqual(90, self.sut.solve("9- 9- 9- 9- 9- 9- 9- 9- 9- 9-"))

    # def test_all_fives_and_spares(self):
    #     self.assertEqual(150, self.sut.solve("5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/5"))

if __name__ == '__main__':
    unittest.main()
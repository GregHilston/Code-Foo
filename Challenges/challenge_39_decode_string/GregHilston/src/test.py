import unittest
from solution import DecodeString

class DecodeStringTests(unittest.TestCase):
    def setUp(self):
        self.sut = DecodeString()

    def test1(self):
        self.assertEqual("aaabcbc", self.sut.solve("3[a]2[bc]"))

    def test2(self):
        self.assertEqual("accaccacc", self.sut.solve("3[a2[c]]"))

    def test3(self):
        self.assertEqual("abcabccdcdcdef", self.sut.solve("2[abc]3[cd]ef"))

if __name__ == '__main__':
    unittest.main()
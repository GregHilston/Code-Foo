import unittest
from solution import GrehgStack, GrehgQueue

class GrehgStackTests(unittest.TestCase):
    def setUp(self):
        self.sut = GrehgStack()

    def test1(self):
        self.assertIsNone(self.sut.push(1), "We should get None back after pushing. Nothing to report.")
        self.assertIsNone(self.sut.push(2), "We should get None back after pushing. Nothing to report.")
        self.assertEqual(2, self.sut.peek(), "The value peeked should be the last item added, as this is a stack FILO")
        self.assertEqual(2, self.sut.pop(), "The value popped should be the last item added, as this is a stack FILO")
        self.assertFalse(self.sut.empty(), "We still have an item in there, item 1")

class GrehgQueueTests(unittest.TestCase):
    def setUp(self):
        self.sut = GrehgQueue()

    def test1(self):
        self.assertIsNone(self.sut.push(1), "We should get None back after pushing. Nothing to report.")
        self.assertIsNone(self.sut.push(2), "We should get None back after pushing. Nothing to report.")
        self.assertEqual(1, self.sut.peek(), "The value peeked should be the first item added, as this is a queue FIFO")
        self.assertEqual(1, self.sut.pop(), "The value popped should be the first item added, as this is a stack FIFO")
        self.assertFalse(self.sut.empty(), "We still have an item in there, item 2")

if __name__ == '__main__':
    unittest.main()
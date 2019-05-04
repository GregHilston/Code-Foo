import unittest
from solution import NewId

class NewIdTests(unittest.TestCase):
    def setUp(self):
        self.sut = NewId()

    def test(self):
        previously_seen_ids = []
        iterations = 10000

        for i in range(iterations):
            new_id = self.sut.solve()

            if new_id in previously_seen_ids:
                self.fail(f"Duplicate new_id {new_id}")

            previously_seen_ids.append(new_id)

if __name__ == '__main__':
    unittest.main()
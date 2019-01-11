import unittest
from solution import CannibalNumbersSolver

class CannibalNumbersSolverTests(unittest.TestCase):
    def test_solver_simple_input_text(self):
        # Given
        input_file_path = "../../input_1.txt"
        self.sut = CannibalNumbersSolver(input_file_path)

        # When
        return_counts = self.sut.solve()

        # Then
        self.assertEqual(2, len(return_counts))
        self.assertEqual(10, return_counts[0])
        self.assertEqual(15, return_counts[1])


if __name__ == '__main__':
    unittest.main()
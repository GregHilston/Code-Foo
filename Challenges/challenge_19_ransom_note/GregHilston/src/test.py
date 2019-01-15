import unittest
from solution import RansomNoteSolver

class RansomNoteSolverTests(unittest.TestCase):
    def test_solver_input_text_1(self):
        # Given
        input_file_path = "../../input_1.txt"
        self.sut = RansomNoteSolver(input_file_path)

        # When
        status = self.sut.solve()

        # Then
        self.assertFalse(status)

    def test_solver_input_text_2(self):
        # Given
        input_file_path = "../../input_2.txt"
        self.sut = RansomNoteSolver(input_file_path)

        # When
        status = self.sut.solve()

        # Then
        self.assertFalse(status)

    def test_solver_input_text_3(self):
        # Given
        input_file_path = "../../input_3.txt"
        self.sut = RansomNoteSolver(input_file_path)

        # When
        status = self.sut.solve()

        # Then
        self.assertTrue(status)

if __name__ == '__main__':
    unittest.main()
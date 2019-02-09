import unittest
from solution import WordPatternSolver

class WordPatternSolverTests(unittest.TestCase):
    def test_solver_input_1(self):
        # Given
        input_file_path = "../../input_1.json"
        sut = WordPatternSolver(input_file_path)

        # When
        output = sut.solve()

        # Then
        self.assertTrue(output)

    def test_solver_input_2(self):
        # Given
        input_file_path = "../../input_2.json"
        sut = WordPatternSolver(input_file_path)

        # When
        output = sut.solve()

        # Then
        self.assertFalse(output)

    def test_solver_input_3(self):
        # Given
        input_file_path = "../../input_3.json"
        sut = WordPatternSolver(input_file_path)

        # When
        output = sut.solve()

        # Then
        self.assertFalse(output)

    def test_solver_input_4(self):
        # Given
        input_file_path = "../../input_4.json"
        sut = WordPatternSolver(input_file_path)

        # When
        output = sut.solve()

        # Then
        self.assertFalse(output)

if __name__ == '__main__':
    unittest.main()
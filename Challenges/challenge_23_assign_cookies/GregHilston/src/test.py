import unittest
from solution import AssignCookiesSolver

class AssignCookiesSolverTests(unittest.TestCase):
    def test_solver_input(self):
        # Given
        input_file_path = "../../input_1.json"
        sut = AssignCookiesSolver(input_file_path)

        # When
        perimeter = sut.solve()

        # Then
        self.assertEqual(1, perimeter)

    def test_solver_input_2(self):
        # Given
        input_file_path = "../../input_2.json"
        sut = AssignCookiesSolver(input_file_path)

        # When
        perimeter = sut.solve()

        # Then
        self.assertEqual(2, perimeter)

    def test_solver_input_3(self):
        # Given
        input_file_path = "../../input_3.json"
        sut = AssignCookiesSolver(input_file_path)

        # When
        perimeter = sut.solve()

        # Then
        self.assertEqual(0, perimeter)

    def test_solver_input_4(self):
        # Given
        input_file_path = "../../input_4.json"
        sut = AssignCookiesSolver(input_file_path)

        # When
        perimeter = sut.solve()

        # Then
        self.assertEqual(0, perimeter)

if __name__ == '__main__':
    unittest.main()
import unittest
from solution import AdditivePersistenceSolver

class AdditivePersistenceSolverTests(unittest.TestCase):
    def test_solver_input(self):
        # Given
        input_file_path = "../../input_1.json"
        sut = AdditivePersistenceSolver(input_file_path)

        # When
        output = sut.solve()

        # Then
        self.assertEqual(1, output)

    def test_solver_input_2(self):
        # Given
        input_file_path = "../../input_2.json"
        sut = AdditivePersistenceSolver(input_file_path)

        # When
        output = sut.solve()

        # Then
        self.assertEqual(2, output)

    def test_solver_input_3(self):
        # Given
        input_file_path = "../../input_3.json"
        sut = AdditivePersistenceSolver(input_file_path)

        # When
        output = sut.solve()

        # Then
        self.assertEqual(2, output)

    def test_solver_input_4(self):
        # Given
        input_file_path = "../../input_4.json"
        sut = AdditivePersistenceSolver(input_file_path)

        # When
        output = sut.solve()

        # Then
        self.assertEqual(3, output)

if __name__ == '__main__':
    unittest.main()
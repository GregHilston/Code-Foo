import unittest
from solution import BuySellStockSolver

class BuySellStockSolverTests(unittest.TestCase):
    def test_solver_input_1(self):
        # Given
        input_file_path = "../../input_1.json"
        self.sut = BuySellStockSolver(input_file_path)

        # When
        max_profit = self.sut.solve()

        # Then
        self.assertEqual(5, max_profit)

    def test_solver_input_2(self):
        # Given
        input_file_path = "../../input_2.json"
        self.sut = BuySellStockSolver(input_file_path)

        # When
        max_profit = self.sut.solve()

        # Then
        self.assertEqual(0, max_profit)

if __name__ == '__main__':
    unittest.main()
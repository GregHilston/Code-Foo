import unittest
from solution import IslandPerimeterSolver

class IslandPerimeterSolverTests(unittest.TestCase):
    def test_solver_input(self):
        # Given
        input_file_path = "../../input.json"
        sut = IslandPerimeterSolver(input_file_path)

        # When
        perimeter = sut.solve()

        # Then
        self.assertEqual(16, perimeter)

    def test_solver_input_1(self):
        # Given
        input_file_path = "../../input_1.json"
        sut = IslandPerimeterSolver(input_file_path)

        # When
        perimeter = sut.solve()

        # Then
        self.assertEqual(4, perimeter)

    def test_solver_input_2(self):
        # Given
        input_file_path = "../../input_2.json"
        sut = IslandPerimeterSolver(input_file_path)

        # When
        perimeter = sut.solve()

        # Then
        self.assertEqual(6, perimeter)

    def test_getAdjacentWaterOfLandRowColumn(self):
        #given 
        input_file_path = "../../input.json"
        sut = IslandPerimeterSolver(input_file_path)
        row = -1
        column = -1
        fakeBoard = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        
        #when
        returnVal = sut.getAdjacentWaterOfLandRowColumn(fakeBoard, row, column)

        #then
        self.assertEqual(0, returnVal)
                
    def test_getAdjacentWaterOfLandRowColumnOfWater(self):
        #given 
        input_file_path = "../../input.json"
        sut = IslandPerimeterSolver(input_file_path)
        row = 1
        column = 1
        fakeBoard = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        
        #when
        returnVal = sut.getAdjacentWaterOfLandRowColumn(fakeBoard, row, column)

        #then
        self.assertEqual(0, returnVal)

    def test_getAdjacentWaterOfLandRowColumnOfLand(self):
        #given 
        input_file_path = "../../input.json"
        sut = IslandPerimeterSolver(input_file_path)
        row = 1
        column = 1
        fakeBoard = [
            [0, 0, 0],
            [0, 1, 0],
            [0, 1, 0]
        ]
        
        #when
        returnVal = sut.getAdjacentWaterOfLandRowColumn(fakeBoard, row, column)

        #then
        self.assertEqual(3, returnVal)

    def test_isNorthWaterWithWater(self):
        #given 
        input_file_path = "../../input.json"
        sut = IslandPerimeterSolver(input_file_path)
        row = 1
        column = 1
        fakeBoard = [
            [0, 0, 0],
            [0, 1, 0],
            [0, 1, 0]
        ]
        
        #when
        returnVal = sut.isNorthWater(fakeBoard, row, column)

        #then
        self.assertEqual(True, returnVal)

    def test_isNorthWaterIsLand(self):
        #given 
        input_file_path = "../../input.json"
        sut = IslandPerimeterSolver(input_file_path)
        row = 2
        column = 1
        fakeBoard = [
            [0, 0, 0],
            [0, 1, 0],
            [0, 1, 0]
        ]
        
        #when
        returnVal = sut.isNorthWater(fakeBoard, row, column)

        #then
        self.assertEqual(False, returnVal)

    def test_isNorthWaterOutOfBounds(self):
        #given 
        input_file_path = "../../input.json"
        sut = IslandPerimeterSolver(input_file_path)
        row = -1
        column = -1
        fakeBoard = [
            [0, 0, 0],
            [0, 1, 0],
            [0, 1, 0]
        ]
        
        #when
        returnVal = sut.isNorthWater(fakeBoard, row, column)

        #then
        self.assertEqual(True, returnVal)

    def test_isNorthWaterOutOfBoundsWhenMathed(self):
        #given 
        input_file_path = "../../input.json"
        sut = IslandPerimeterSolver(input_file_path)
        row = 0
        column = 1
        fakeBoard = [
            [0, 1, 0],
            [0, 1, 0],
            [0, 1, 0]
        ]
        
        #when
        returnVal = sut.isNorthWater(fakeBoard, row, column)

        #then
        self.assertEqual(True, returnVal)

if __name__ == '__main__':
    unittest.main()
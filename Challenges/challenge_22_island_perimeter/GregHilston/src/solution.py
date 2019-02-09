import sys
import json

class IslandPerimeterSolver():
    def __init__(self, input_file_path):
        self.input_file_path = input_file_path

    def parse_input(self):
        with open(self.input_file_path) as f:
            data = json.load(f)

            return data["board"]

    def solve(self):
        perimeter = 0
        board = self.parse_input()

        for row, list in enumerate(board):
            for column, number in enumerate(list):
                current_perimeter = 0
                current_perimeter = self.getAdjacentWaterOfLandRowColumn(board, row, column)
                perimeter += current_perimeter
        return perimeter

    def getAdjacentWaterOfLandRowColumn(self, board, row, column):
        # IF NOT LAND, RETURN 0
        try:
            if board[row][column] != 1:
                return 0
        except:
            # out of bounds
            return 0

        count = 0

        if self.isNorthWater( board, row, column):
            count += 1

        if self.isSouthWater( board, row, column):
            count += 1

        if self.isEastWater( board, row, column):
            count += 1

        if self.isWestWater( board, row, column):
            count += 1
        return count

    def isNorthWater(self, board, row, column):
        row -= 1
        if row < 0:
            # woops, a real out of bounds check
            return True
        try:
            if board[row][column] == 0:
                return True 
        except:
            # out of bounds, water by default
            return True
        return False

    def isEastWater(self, board, row, column):
        column += 1

        try:
            if board[row][column] == 0:
                return True 
        except:
            # out of bounds, water by default
            return True
        return False

    def isSouthWater(self, board, row, column):
        row += 1

        try:
            if board[row][column] == 0:
                return True 
        except:
            # out of bounds, water by default
            return True
        return False

    def isWestWater(self, board, row, column):
        column -= 1

        if column < 0:
            # woops, a real out of bounds check
            return True
        try:
            if board[row][column] == 0:
                return True 
        except:
            # out of bounds, water by default
            return True
        return False

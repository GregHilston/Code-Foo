import sys

class RansomNoteSolver():
    def __init__(self, input_file_path):
        self.input_file_path = input_file_path

    def parse_input(self):
        """Parses the input from the input file separating letters needed and 
        available.
        
        Returns:
            list, list:  Contains all letters needed and available.

        """
        LETTERS_NEEDED_LINE_INDEX = 0
        LETTERS_AVAILABLE_LINE_INDEX = 1

        with open(self.input_file_path) as f:
            lines = f.readlines()

            letters_needed = list(lines[LETTERS_NEEDED_LINE_INDEX])
            letters_available = list(lines[LETTERS_AVAILABLE_LINE_INDEX])

            return letters_needed, letters_available

    def solve(self):
        """Determines whether all the letters given from a magazine are enough to
        form our desired ransom note.
        
        Returns:
            bool: True if we can create our ransom note, else false.

        """
        letters_needed, letters_available = self.parse_input()

        for letter_needed in letters_needed:
            if letter_needed in letters_available:
                letters_available.remove(letter_needed)
            else:
                return False # we needed a letter we didn't have

        return True
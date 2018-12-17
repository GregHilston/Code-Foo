import os.path

INPUT_FILE_PATH = "../input_1.txt"

class TicTacToeBoard:
    """Reads an input file, creates and inner state of a tic tac toe board
    and can display it visually. Throws ValueError exception if the input file
    is invalid.
    """

    NUMBER_OF_EXPECTED_LINES = 1
    ACCEPTABLE_CHARACTERS = ['-', 'x', 'o']

    def __init__(self, INPUT_FILE_PATH):
        """Constructs the internal state of our board and performs validation
        checks.
        
        Arguments:
            INPUT_FILE_PATH {[str]} -- [path to our input file]
        """

        self.INPUT_FILE_PATH = INPUT_FILE_PATH

        self.validate_input_file()
        self.board = self.parse_board()

    def validate_input_file(self):
        """Validates the input file, throwing an ValueError Exception
        if any unexpected situations occur.
        """

        if not os.path.exists(self.INPUT_FILE_PATH):
            raise ValueError(f"Input file path {INPUT_FILE_PATH} does not exist")

        if not os.path.isfile(self.INPUT_FILE_PATH):
            raise ValueError(f"Input file path {self.INPUT_FILE_PATH} is not a file")

        if self.file_len(self.INPUT_FILE_PATH) != self.NUMBER_OF_EXPECTED_LINES:
            raise ValueError(f"Input file {self.INPUT_FILE_PATH} has more than {self.NUMBER_OF_EXPECTED_LINES} line(s)")    


    def file_len(self, fname):
        """Determines how many lines are in a file
        
        Arguments:
            fname {str} -- filename to read
        
        Returns:
            int -- number of lines in a file
        """

        with open(fname) as f:
            for i, l in enumerate(f):
                pass
        return i + 1

    def parse_board(self):
        """parses the input file and builds up our internal representation of the 
        game state
        
        Returns:
            [int] -- board representation
        """

        EXPECTED_NUMBER_OF_CHARACTERS = 9
        board = []

        for line in open(self.INPUT_FILE_PATH):
            for character in line.split(","):
                if character not in self.ACCEPTABLE_CHARACTERS:
                    raise ValueError(f"Unexpected character {character}. Acceptable characters {self.ACCEPTABLE_CHARACTERS}")
            
                board.append(character)

        if len(board) != EXPECTED_NUMBER_OF_CHARACTERS:
            raise ValueError(f"Unexpected number of characters {len(board)}. Expected {EXPECTED_NUMBER_OF_CHARACTERS}")

        return board

    def __str__(self):
        """Converts the internal representation of the board to a 
        str format
        
        Returns:
            str -- str representation of board
        """

        CHARACTERS_PER_LINE = 3
        CHARACTER_SEPARATOR = ' '
        NEWLINE_SEPARATOR = '\n'
        i = 0
        s = ""

        for character in self.board:
            if i != 0 and i % CHARACTERS_PER_LINE == 0:
                s += NEWLINE_SEPARATOR

            i += 1
            s += character + CHARACTER_SEPARATOR

        return s

tic_tac_toe_board = TicTacToeBoard(INPUT_FILE_PATH)
print(tic_tac_toe_board)

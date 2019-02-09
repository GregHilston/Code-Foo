import sys
import json

class WordPatternSolver():
    def __init__(self, input_file_path):
        self.input_file_path = input_file_path

    def parse_input(self):
        with open(self.input_file_path) as f:
            data = json.load(f)

            return data["pattern"], data["str"]

    def solve(self):
        pattern, string = self.parse_input()

        words = string.split(' ')

        pattern_to_string = {}
        string_to_pattern = {}

        for letter, word in zip(pattern, words):
            if letter in pattern_to_string and pattern_to_string[letter] != word:
                return False
            pattern_to_string[letter] = word

            if word in string_to_pattern and string_to_pattern[word] != letter:
                return False
            string_to_pattern[word] = letter
        
        return True
import sys
import json

class AdditivePersistenceSolver():
    def __init__(self, input_file_path):
        self.input_file_path = input_file_path

    def parse_input(self):
        with open(self.input_file_path) as f:
            data = json.load(f)

            return data["input"]

    def solve(self):
        iteration_count = 0

        input = self.parse_input()

        while True:
            sum = 0
            iteration_count += 1

            for number in str(input):
                sum += int(number)

            if len(str(sum)) == 1:
                return iteration_count

            input = sum
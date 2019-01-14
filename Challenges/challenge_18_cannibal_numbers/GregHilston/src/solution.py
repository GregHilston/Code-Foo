import sys

class CannibalNumbersSolver():
    def __init__(self, input_file_path):
        self.input_file_path = input_file_path

    def parse_input(self):
        """Parses the input from the input file.
        
        Returns:
            list, list:  Contains all parses values as a list and queries as a list.

        """
        SKIP_FIRST_LINE = 1

        with open(self.input_file_path) as fp:
            lines = fp.readlines()[SKIP_FIRST_LINE:]

            values = list(map(int, lines[0].split(' ')))
            queries = list(map(int, lines[1].split(' ')))

            return values, queries

    def next_index_to_process(self, values, target):
        """Returns the index of the number closest to the target without being equal or greater. 
        If no values are available, returns -1.
        
        Args:
            values list: The values to process.
            target int: The target we're trying to get to.

        Returns:
            int: Index of next value to process or -1 if none are found.
            
        """
        current_best_distance = sys.maxsize # everything should beat this
        current_best_index = -1 # we use negative 

        for index, value in enumerate(values):
            # print(f"evaluating index {index} value {value}")
            # print(f"\tcurrent_best_distance {current_best_distance}")
            # print(f"\tcurrent_best_index {current_best_index}")
            distance_to_target = target - value

            if distance_to_target > 0 and distance_to_target < current_best_distance:
                # print(f"\t\ttaking this, which has a distance_to_target of {distance_to_target}!")
                current_best_distance = distance_to_target
                current_best_index = index
        # print(f"current_best_index {current_best_index}")
        return current_best_index

    def have_index_consume(self, values, index):
        # print(f"increasing {values[index]} by one by canabalizing {values[values.index(min(values))]}")
        
        values[index] += 1 # increase value by one

        del values[values.index(min(values))] # cannabalize smallest number

        # print(f"\tnew values {values}")
        return values
        
    def number_of_values_over_target(self, values, target):
        return sum(i >= target for i in values)

    def solve_query(self, values, target):
        """Solves a query.
        
        Args:
            values (list): The values to process.
            query (list): The target amount.
        
        Returns:
            int: The best amount of values above the query we can find.

        """

        while True:
            next_index = self.next_index_to_process(values, target)
            if next_index == -1:
                # print(f"Solved query with answer of {self.number_of_values_over_target(values, target)}")
                return self.number_of_values_over_target(values, target)
            else:
                values = self.have_index_consume(values, next_index)


    def solve(self):
        """Solves all the queries from the input file, glueing together all logic.
        
        Returns:
            list(int): Our solutions to the queries.

        """
        answers = []
        values, queries = self.parse_input()

        for query in queries:
            # print(f"query: {query}")
            answers.append(self.solve_query(values.copy(), query))
        
        return answers
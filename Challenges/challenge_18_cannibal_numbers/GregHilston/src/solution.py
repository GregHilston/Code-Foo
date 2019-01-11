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

            values = lines[0].split(' ')
            queries = lines[1].split(' ')

            return values, queries

    def solve_query(self, values, query):
        """Solves a query.
        
        Args:
            values (list): The values to process.
            query (list): The target amount.
        
        Returns:
            int: The best amount of values above the query we can find.

        """
        return 0

    def solve(self):
        """Solves all the queries from the input file, glueing together all logic.
        
        Returns:
            list(int): Our solutions to the queries.

        """
        answers = []
        values, queries = self.parse_input()

        for query in queries:
            answers.append(self.solve_query(values, query))
        
        return answers
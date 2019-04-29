class NimGame:
    def solve(self, starting_amount: int) -> bool:
        """Determines if I will win this game, going first, with a certain start_amount
        """

        return starting_amount % 4 != 0
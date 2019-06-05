class BulbSwitcher:
    def __init__(self):
        pass

    def solve(self, number_of_bulbs_and_rounds: int) -> int:
        # base case cause I'm lazy
        if number_of_bulbs_and_rounds == 1:
            return 1

        # let -1 = OFF
        # let 1 = ON
        bulbs = [-1 for i in range(number_of_bulbs_and_rounds)]

        print(f"Starting simulation where number_of_bulbs_and_rounds: {number_of_bulbs_and_rounds}, bulbs: {bulbs}")

        for round in range(1, number_of_bulbs_and_rounds + 1):
            print(f"\tBeginning round {round}, bulbs: {bulbs}")
            print(f"\tLooking to flip bulb's at every {round} index")

            first_index = round - 1
            print(f"\t\tfirst_index {first_index}")
            print(f"\t\tend_index {number_of_bulbs_and_rounds}")
            print(f"\t\tstep {round}")

            for bulb_index in range(first_index, number_of_bulbs_and_rounds, round):
                bulbs[bulb_index] = -1 * bulbs[bulb_index]
                print(f"\t\t\tFlipping bulb {bulb_index} from {bulbs[bulb_index]} to {-1 * bulbs[bulb_index]}")
            print(f"\tEnding round {round}, bulbs: {bulbs}")
        return len(list(filter(lambda x: x != -1, bulbs)))
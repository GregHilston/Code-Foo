class BulbSwitcher:
    def __init__(self):
        pass

    def solve(self, number_of_bulbs_and_rounds: int) -> int:
        # let -1 = OFF
        # let 1 = ON
        # this is because we are lazy and can flip the numbers easily and sum the total number of 1's later
        bulbs = [1 for i in range(number_of_bulbs_and_rounds)] # simulate first round automatically

        print(f"After first round, the {number_of_bulbs_and_rounds} bulbs: {bulbs}")

        for current_round in range(1, number_of_bulbs_and_rounds - 1):
            ith_bulb_to_flip = current_round + 1
            print(f"\tith_bulb_to_flip = {ith_bulb_to_flip}")

            # flip the correct bulbs
            for potential_bulb_to_flip in range(number_of_bulbs_and_rounds):
                if potential_bulb_to_flip  % ith_bulb_to_flip == 0:
                    print(f"\t\tflipping bulb {potential_bulb_to_flip}")
                    bulbs[potential_bulb_to_flip] = -1 * bulbs[potential_bulb_to_flip]
            print(f"\t\t\tAfter round {current_round + 1}, bulbs: {bulbs}")

        return len(list(filter(lambda x: x != -1, bulbs)))
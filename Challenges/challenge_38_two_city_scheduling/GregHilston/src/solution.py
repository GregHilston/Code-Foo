class TwoCityScheduling:
    city_a_index = 0
    city_b_index = 1
    savings_by_going_to_city_b_index = 2

    def __init__(self):
        pass

    def savings_by_going_to_city_b(self, cost: [[int]]) -> int:
        return cost[self.city_b_index] - cost[self.city_a_index]

    def solve(self, costs: [[int]]) -> int:
        city_a = []
        city_b = []

        # Initial plan to send everyone to City A
        city_a = [i for i in costs]

        # Calculate all savings by switching from City A to City B
        for person in city_a:
            person.append(self.savings_by_going_to_city_b(person))

        # Reschedule half of the A City individuals to B City
        # Selecting the smallest number, representing the biggest gain in savings
        number_of_individuals_to_switch_from_city_a_to_city_b = int(len(costs) / 2)
        for i in range(number_of_individuals_to_switch_from_city_a_to_city_b):
            # calculate all savings
            savings = [j[self.savings_by_going_to_city_b_index] for j in city_a]

            # find max savings, min here as negative numbers represent reduced cost
            max_savings_value = min(savings)

            # find index of max savings
            max_savings_index = savings.index(max_savings_value)

            # move that respected person from City A to City B
            city_b.append(city_a.pop(max_savings_index))

        # Calculate total cost
        return sum([j[self.city_a_index] for j in city_a]) + sum([j[self.city_b_index] for j in city_b])
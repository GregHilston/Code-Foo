class CountingBits:
    def number_of_ones_in_int_as_binary(self, numby: int):
        binary_representation = "{0:b}".format(numby)

        one_count = 0
        for i in binary_representation:
            one_count += int(i)

        return one_count

    def solve(self, n: int):
        number_of_ones_in_each_index = []

        for i in range(n + 1):
            number_of_ones_in_each_index.append(self.number_of_ones_in_int_as_binary(i))

        return number_of_ones_in_each_index
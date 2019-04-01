class RecursiveMultiply:
    def multiply(self, multiplicand: int, multiplier: int, running_sum: int):
        if multiplier == 0:
            return running_sum

        return self.multiply(multiplicand, multiplier - 1, running_sum + multiplicand)

    def recursive_multiply(self, multiplicand: int, multiplier: int):
        return self.multiply(multiplicand, multiplier, 0)
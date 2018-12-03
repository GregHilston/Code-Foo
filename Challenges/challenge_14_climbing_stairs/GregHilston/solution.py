class Solution:
    def print_explanation(self, unique_steps):
        print(f"\t\tThere are {len(unique_steps)} ways to climb to the top.")

        for index, unique_step in enumerate(unique_steps):
            built_up_string = ""

            built_up_string + f"{index + 1}. "

            for step in unique_step:
                if step == 1:
                    built_up_string += "+ 1 step "
                elif step == 2:
                    built_up_string += "+ 2 steps"

        print("\t\t\t" + built_up_string)


    def take_step(self, steps, n):
        """
        :type steps: list
        :type n: int
        :rtype: int
        """
        
        print("\ttake_step has been called with steps = " + str(steps))
        print("\ttake_step has been called with n = " + str(n) + '\n')
        # base case
        if n == 0:
            print("\t\tbase case boi")
            return steps
        # can only take one step   
        elif n == 1: 
            return self.take_step(steps + [1], n-1)
        # can take one step OR two steps
        else: 
            return [self.take_step(steps + [1], n-1), self.take_step(steps + [2], n-2)]
    
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        print("climbStairs has been called with n = " + str(n))
        unique_steps = self.take_step([], n)

        print(f"\t\tunique_steps {unique_steps}")
        self.print_explanation(unique_steps)

        return len(unique_steps)

solution = Solution()

solution.climbStairs(3)

# for i in range(20):
#     solution.climbStairs(i)
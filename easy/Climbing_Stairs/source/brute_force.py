class Solution:

    def climb_stairs(self, i, n):
        # if the number of steps does not match with the N
        if i > n:
            return 0

            # if the number of steps match with the N
        if i == n:
            return 1

            # steps can be either odd or even numbers
        return self.climb_stairs(i + 1, n) + self.climb_stairs(i + 2, n)

    def climbStairs(self, n: int) -> int:
        # invoke the recursive function
        return self.climb_stairs(0, n)
class Solution:

    def climb_stairs(self, i, n, memo):
        if i > n:
            return 0

        if i == n:
            return 1

        if memo[i]:
            return memo[i]

        memo[i] = self.climb_stairs(i + 1, n, memo) + self.climb_stairs(i + 2, n, memo)
        return memo[i]

    def climbStairs(self, n: int) -> int:
        memo = [None for i in range(n + 1)]
        return self.climb_stairs(0, n, memo)

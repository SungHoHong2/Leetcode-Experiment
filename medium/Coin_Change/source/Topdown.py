class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # set the coins as a global variable
        self.coins = coins
        # set up the dp table to record the number of required coins according to the amount
        dp = [None for _ in range(amount + 1)]
        # base case: when the amount is zero then amount of required coins is zero
        dp[0] = 0
        # collect the answer from the top down
        ans = self.topdown(dp, amount)
        # return the answer or -1 if the coins do not sum up to the amount
        return ans if ans != float('inf') else -1

    def topdown(self, dp, remain):
        # return infinite if the coins do not sum up to the amount
        if remain < 0:
            return float('inf')
        # return the recorded result if the answer is cached in the dp table
        if dp[remain] != None:
            return dp[remain]
        # set the variable to record the minimum number of coins
        ans = float('inf')
        # iterate the coins
        for coin in self.coins:
            # get the smallest number of coins that sum up to the remaining amount
            ans = min(ans, self.topdown(dp, remain - coin))
        # update the number of coins that sum up to the amount in the dp table
        dp[remain] = ans + 1
        # return result
        return dp[remain]
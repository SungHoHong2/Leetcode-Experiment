class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # set the array to record the results of each amount
        dp = [float("inf") for i in range(0, amount + 1)]
        # if total amount is zero there is zero coins
        dp[0] = 0
        # iterate the amount by one
        for i in range(1, amount + 1):
            # iterate through the coins
            for j in range(0, len(coins)):
                # if the coins can fit with the amount
                if coins[j] <= i:
                    # update the answer by adding or without the coins
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1)
        # return the minimum number of coins or -1 if invalid
        return dp[amount] if dp[amount] <= amount else -1
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # set the array to record the results of each amount
        dp = [float('inf') for _ in range(amount+1)]
        # if total amount is zero there is zero coins
        dp[0] = 0
        # iterate the coins
        for coin in coins:
            # iterate the amount that fits into the current coin
            for amt in range(coin, amount + 1):
                # update the answer by adding or without the coins
                dp[amt] = min(dp[amt],dp[amt-coin]+1)
        # return the minimum number of coins or -1 if invalid
        return dp[amount] if dp[amount] != float('inf') else -1
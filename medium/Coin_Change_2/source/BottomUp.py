class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # set up the table for keeping records of possible combinations
        dp = [0 for i in range(amount + 1)]
        # if the amount is zero then there is one combination
        dp[0] = 1
        # iterate the coins
        for coin in coins:
            for i in range(coin, amount + 1):
                # accumulate the previous combination without the new coin
                dp[i] += dp[i - coin]
        # return the possible number of combination to reach the result
        return dp[amount]



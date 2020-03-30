class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # create the table of answers (0 ~ amount)
        dp = [float("inf") for i in range(0, amount + 1)]

        # start from zero
        dp[0] = 0

        # iterate through the table
        for i in range(1, amount + 1):

            # iterate through the coins
            for j in range(0, len(coins)):
                # if the coins match the answer
                if coins[j] <= i:
                    # update the answer with the total number of used coins
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1)

        # if the final answer is invalid
        if dp[amount] > amount:
            # return -1
            return -1
        # if the final answer is valid
        else:
            # return result
            return dp[amount]
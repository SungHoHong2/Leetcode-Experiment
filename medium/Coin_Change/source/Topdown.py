class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # create the cache to record the results
        self.count = [None for i in range(0, amount + 1)]
        # base case: when the amount is zero then amount of required coins is zero
        self.count[0] = 0
        # invoke the recursion
        return self.topdown(coins, amount)

    def topdown(self, coins, remain):
        # return false if there is no matching accumulation of coins
        if remain < 0:
            return -1
            # return the recorded result if the answer is already explored
        if self.count[remain] != None:
            return self.count[remain]
        # set the min variable to get the minimum collection of coins to match the amount
        min = float('inf')
        # iterate the coins
        for coin in coins:
            # get the number of possible coins from the recursion
            res = self.topdown(coins, remain - coin)
            # Update the min value if the result is valid (note that need to + 1 for the final result)
            if 0 <= res < min:
                min = 1 + res
        # record -1 if the min is invalid
        if min == float('inf'):
            self.count[remain] = -1
        # record the min if the min is valid
        else:
            self.count[remain] = min
        # return the number of coins that are required to match the amount
        return self.count[remain]

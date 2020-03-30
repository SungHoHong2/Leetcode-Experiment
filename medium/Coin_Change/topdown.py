class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # create the cache
        self.count = [0 for i in range(0, amount)]

        # initiate the topdown (coins, amount)
        return self.topdown(coins, amount)

    def topdown(self, coins, remain):

        # if the remain is invalid
        if remain < 0:
            # return false
            return -1

        # if the remain is zero
        if remain == 0:
            # return zero
            return 0

        # if the remain is already explored
        if self.count[remain - 1] != 0:
            # return the cached result
            return self.count[remain - 1]

        # allocate the min
        min = float("inf")

        # iterate the coins
        for coin in coins:
            # the number of coin changes
            res = self.topdown(coins, remain - coin)

            # if the result is valid
            if res >= 0 and res < min:
                # update the min with (result + 1)
                min = 1 + res

        # if the min is invalid
        if min == float("inf"):
            # assign it as -1
            self.count[remain - 1] = -1
        # if the min is valid
        else:
            # assign the min
            self.count[remain - 1] = min

        # return the min
        return self.count[remain - 1]
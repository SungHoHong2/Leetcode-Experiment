class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount < 1:
            return 0

        self.count = [0 for i in range(0, amount)]
        return self.topdown(coins, amount)

    def topdown(self, coins, remain):
        if remain < 0:
            return -1
        if remain == 0:
            return 0

        if self.count[remain - 1] != 0:
            return self.count[remain - 1]

        min = float("inf")

        for coin in coins:

            # the number of coin changes
            res = self.topdown(coins, remain - coin)
            if res >= 0 and res < min:
                min = 1 + res

        if min == float("inf"):
            self.count[remain - 1] = -1
        else:
            self.count[remain - 1] = min

        return self.count[remain - 1]
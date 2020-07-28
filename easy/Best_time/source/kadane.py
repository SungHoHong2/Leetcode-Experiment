class Solution(object):
    def maxProfit(self, prices):
        # set up the current profit
        currProfit = 0
        # set up the maximum profit
        maxProfit = 0
        # iterate the prices
        for i in range(1, len(prices)):
            # aggregate the current profit
            currProfit += prices[i] - prices[i - 1]
            # set the current profit to zero if it reaches negative
            currProfit = max(0, currProfit)
            # keep track of the maximum profit
            maxProfit = max(currProfit, maxProfit)
        # return the maximum profit
        return maxProfit
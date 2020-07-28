class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # set the tracker for the most minimum price
        minprice = float("inf")
        # set the maximum profit (return value)
        maxprofit = 0
        # iterate the available prices
        for i in range(0, len(prices)):
            # keep track of the lowest minimum price
            if prices[i] < minprice:
                minprice = prices[i]
            # keep track of the highest maximum profit
            elif prices[i] - minprice > maxprofit:
                maxprofit = prices[i] - minprice
        # return the maximum profit
        return maxprofit
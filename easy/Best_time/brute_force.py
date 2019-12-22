class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Say you have an array for which the ith element is the price of a given stock on day i.
        # If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

        benefit = 0

        for i in range(0, len(prices) - 1):
            for s in range(i + 1, len(prices)):
                temp = prices[s] - prices[i]
                # print(benefit, prices[i], prices[s])

                if benefit < temp:
                    benefit = temp

        return benefit


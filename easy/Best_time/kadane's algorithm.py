class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxC = 0
        maxP = 0
        for i in range(1, len(prices)):
            maxC += prices[i] - prices[i - 1]
            maxC = max(0, maxC)
            maxP = max(maxC, maxP)

        return maxP
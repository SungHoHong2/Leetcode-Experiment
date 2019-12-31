class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minV = float("inf")
        maxP = 0
        for i in range(len(prices)):
            if prices[i] < minV:
                minV = prices[i]
            elif prices[i] - minV > maxP:
                maxP = prices[i] - minV
        return maxP
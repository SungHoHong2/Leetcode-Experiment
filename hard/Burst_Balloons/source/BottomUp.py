class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # reframe problem as before
        nums = [1] + nums + [1]
        # get the total length of the input
        n = len(nums)
        # dp will store the results of our calls
        dp = [[0 for x in range(n)] for y in range(n)]
        # expand the scope of dp from the [n-2:n] items numbers to all items [0:n]
        for left in range(n-2, -1, -1):
            for right in range(left+2, n):
                # dp formula
                dp[left][right] = max(nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right] for i in range(left+1, right))
        # return the final result of the dp [0:n]
        return dp[0][n-1]

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # reframe the input
        nums = [1] + nums + [1]
        # get the total length of the input
        n = len(nums)
        # set the dp table that stores maximum score for within the range of left and right
        dp = [[0 for left in range(n)] for right in range(n)]
        # start computing the dp from the rightmost side
        for left in range(n-2, -1, -1):
            for right in range(left+2, n):
                score = 0
                for i in range(left+1, right):
                    score = max(score, nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right])
                dp[left][right] = score
        # return the largest score between the first and the last balloon
        return dp[0][n-1]
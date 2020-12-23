class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        # set the total length of the input
        n = len(nums)
        # set a dp table using columns as the number of subsets and n as the inputs in the array
        dp = [[float('inf') for i in range(m+1)] for j in range(n+1)]
        sub = [0 for i in range(n+1)]
        # create an array to easily create the potential jth subset
        for i in range(n):
            sub[i+1] = sub[i] + nums[i]
        # set the smallest maximum subset to zero when array is zero
        dp[0][0] = 0
        # expanding the range of the array
        for i in range(1, n+1):
            # expanding the number of subsets
            for j in range(1, m+1):
                # get the minimum part
                for k in range(0, i):
                    # smallest maximum sum by comparing the j-1 subsets with potential jth subsets
                    dp[i][j] = min(dp[i][j], max(dp[k][j-1], sub[i]-sub[k]))
        # return the smallest maximum subset
        return dp[n][m]

class Solution:

    def canJump(self, nums: List[int]) -> bool:

        dp = [False for i in nums]
        dp[0] = True
        right = 0

        for i in range(len(nums)):
            if dp[i]:
                for j in range(right, min(len(nums) - 1, i + nums[i]) + 1):
                    dp[j] = True
                    right = j

        return dp[len(nums) - 1]

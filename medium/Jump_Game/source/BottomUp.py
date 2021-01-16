class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # set the dp table
        dp = [False for i in nums]
        # base case: final index reaches the destination
        dp[len(nums) - 1] = True
        # iterate the input backwards
        for i in range(len(nums) - 2, -1, -1):
            # iterate all the possible jumps from the current position
            max_jump = min(i + nums[i], len(nums) - 1)
            # record the dp table as true if the jump reaches the destination
            for jump in range(i + 1, max_jump + 1):
                if dp[jump]:
                    dp[i] = True
                    break
        # return if the destination is reachable from the first index
        return dp[0]
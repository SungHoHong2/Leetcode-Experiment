class Solution:
    def TopDown(self, position, nums):
        # return the dp table if the index is explored
        if self.dp[position] != None:
            return self.dp[position]
        # get the maximum jump of the current index
        max_jump = min(position + nums[position], len(nums) - 1)
        # iterate all the possible jumps from the current position
        for jump in range(position + 1, max_jump + 1):
            # record the dp table as true if the jump reaches the destination
            if self.TopDown(jump, nums):
                self.dp[position] = True
                return True
        # record the dp table as false
        self.dp[position] = False
        return False

    def canJump(self, nums: List[int]) -> bool:
        # set up the dp table
        self.dp = [None for _ in nums]
        # base case: final index reaches the destination
        self.dp[len(nums) - 1] = True
        # invoke the top up approach
        return self.TopDown(0, nums)
class Solution:

    def canJumpFromPosition(self, position, nums):

        if self.memo[position] != None:
            return self.memo[position]

        availableJump = min(position + nums[position], len(nums) - 1)
        for nextPosition in range(position + 1, availableJump + 1):
            if self.canJumpFromPosition(nextPosition, nums):
                self.memo[position] = True
                return True

        self.memo[position] = False
        return False

    def canJump(self, nums: List[int]) -> bool:

        self.memo = [None for i in nums]
        self.memo[len(nums) - 1] = True
        return self.canJumpFromPosition(0, nums)
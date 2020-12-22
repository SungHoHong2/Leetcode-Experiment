class Solution:

    def canJump(self, nums: List[int]) -> bool:

        memo = [False for i in nums]
        memo[len(nums) - 1] = True

        for i in range(len(nums) - 2, -1, -1):
            furthestJump = min(i + nums[i], len(nums) - 1)
            for j in range(i + 1, furthestJump + 1):
                if memo[j]:
                    memo[i] = True
                    break

        return memo[0]


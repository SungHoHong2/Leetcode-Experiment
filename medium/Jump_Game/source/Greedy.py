class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # set the last position
        lastPos = len(nums) - 1
        # iterate the input backwards
        for i in range(len(nums) - 1, -1, -1):
            # update the last position if the possible jump can reach the last position
            if i + nums[i] >= lastPos:
                lastPos = i
        # return true if the last position reaches the starting point
        return lastPos == 0
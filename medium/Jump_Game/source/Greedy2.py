class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        # max position one could reach
        # starting from index <= i
        max_pos = nums[0]

        for i in range(1, n):
            # if one could't reach this point
            if max_pos < i:
                return False
            max_pos = max(max_pos, nums[i] + i)

        return True
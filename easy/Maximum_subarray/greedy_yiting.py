class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur_max = max_sum = float("-inf")

        for i in range(len(nums)):
            cur_max = max(cur_max + nums[i], nums[i])
            max_sum = max(max_sum, cur_max)
        return max_sum
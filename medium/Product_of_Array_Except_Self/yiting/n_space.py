class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        L = [1] * len(nums)
        R = [1] * len(nums)
        result = [1] * len(nums)
        L[0] = 1
        R[-1] = 1

        for i in range(1, len(nums)):
            L[i] = nums[i - 1] * L[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            R[i] = nums[i + 1] * R[i + 1]

        for i in range(len(nums)):
            result[i] = L[i] * R[i]

        return result

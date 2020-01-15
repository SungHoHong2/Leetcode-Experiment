class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result = 0
        s = [0] * (len(nums) + 1)
        s[0] = 0
        for i in range(1, len(s)):
            s[i] = s[i - 1] + nums[i - 1]

        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                if s[j] - s[i] == k:
                    result += 1

        return result
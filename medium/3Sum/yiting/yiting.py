class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        dict = {}
        result = set()
        nums.sort()
        for i in range(len(nums)):
            dict[nums[i]] = i

        for i in range(len(nums)):
            target = 0 - nums[i]
            for j in range(i + 1, len(nums)):
                tmp1 = target - nums[j]
                if tmp1 in dict and dict[tmp1] > j:
                    result.add((nums[i], nums[j], tmp1))

        return result



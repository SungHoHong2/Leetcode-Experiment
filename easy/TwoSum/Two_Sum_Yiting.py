class Solution(object):
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return []
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic:
                return [dic[nums[i]],i]
            else:
                dic[target - nums[i]] = i
class Solution:
    def kSum(self, nums: List[int], target: int, k: int) -> List[List[int]]:
        # set a list that stores the group of four integers that sums up to the target
        res = list()
        # return the empty list if there is no more input
        if len(nums) == 0:
            return res
        # return empty list if smallest or largest possible sum does not cannot reach the target
        if nums[0] * k > target or target > nums[-1] * k:
            return res
            # return the result from the twoSum if 2 numbers need to match the target
        if k == 2:
            return self.twoSum(nums, target)
        # iterate the index
        for i in range(len(nums)):
            # if it is the first index or not duplicated
            if i == 0 or nums[i - 1] != nums[i]:
                # append the current number with the the recursion using reduced target and k
                for ans in self.kSum(nums[i + 1:], target - nums[i], k - 1):
                    res.append([nums[i]] + ans)
        # return the collection of answers
        return res

    def twoSum(self, nums, target):
        # set a return array
        res = list()
        # create a hashset
        cache = set()
        # set the index of the leftmost element that is at the rightside of the current element
        left, right = 0, len(nums)
        # loop until the indexes converge
        while left < right:
            # calculate the complement
            complement = target - nums[left]
            # if the complement is not in the memory
            if complement not in cache:
                # record the current element
                cache.add(nums[left])
                # increase the leftmost index
                left += 1
                # if the complement is in the memory
            else:
                # add the answer to the return list
                res.append([nums[left], complement])
                # increase the leftmost index
                left += 1
                # skip the leftmost indexes that are duplicates
                while left < right and nums[left - 1] == nums[left]:
                    left += 1
        # return an array
        return res

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # sort the input in ascending order
        nums.sort()
        # invoke the recursion
        return self.kSum(nums, target, 4)
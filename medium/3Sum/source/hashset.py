class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # set the return array that contains the elements that sum up to zero
        res = list()
        # assume that the input array is already sorted
        nums.sort()
        # iterate the numbers
        for i in range(len(nums)):
            # if the twoSum2 cannot produce zero anymore
            if nums[i] > 0:
                # finish iteration
                break
            # if the first element or the neighboring element is not the same
            if i == 0 or nums[i - 1] != nums[i]:
                # invoke the twoPointer function
                self.twoSum2(nums, i, res)
        # return the answers
        return res

    def twoSum2(self, nums: List[int], i: int, res: List[List[int]]):
        # create a hashset
        cache = set()
        # set the index of the leftmost element that is at the rightside of the current element
        left, right = i + 1, len(nums)
        # loop until the indexes converge
        while left < right:
            # calculate the complement
            complement = 0 - nums[i] - nums[left]
            # if the complement is not in the memory
            if complement not in cache:
                # record the current element
                cache.add(nums[left])
                # increase the leftmost index
                left += 1
                # if the complement is in the memory
            else:
                # add the answer to the return list
                res.append([nums[i], complement, nums[left]])
                # increase the leftmost index
                left += 1
                # skip the leftmost indexes that are duplicates
                while left < right and nums[left - 1] == nums[left]:
                    left += 1
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # set the return array
        res = list()
        # assume that the array is already sorted
        nums.sort()
        # iterate the array
        for i in range(len(nums)):
            # if the current element is above zero
            if nums[i] > 0:
                # stop the iteration
                break
                # if the element is the first or not duplicated
            if i == 0 or nums[i - 1] != nums[i]:
                # invoke the twoSum function
                self.twoSum(nums, i, res)
        # return the result
        return res

    def twoSum(self, nums: List[int], i: int, res: List[List[int]]):
        # create a hashset
        hashset = set()
        # set the index of the leftmost element that is at the rightside of the current element
        left = i + 1
        # iterate the array
        while left < len(nums):
            # calculate the complement
            complement = 0 - nums[i] - nums[left]
            # if the complement is not in the memory
            if complement not in hashset:
                # record the current element
                hashset.add(nums[left])
                # increase the leftmost index
                left += 1
                # if the complement is in the hashset
            else:
                # add the answer to the return list
                res.append([nums[i], nums[left], complement])
                # increase the leftmost index
                left += 1
                # skip the leftmost indexes that are duplicates
                while left < len(nums) and nums[left - 1] == nums[left]:
                    left += 1

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # set the return array that contains the elements that sum up to zero
        res = list()
        # assume that the input array is already sorted
        nums.sort()
        # iterate the numbers
        for i in range(len(nums)):
            # if the current index is above zero
            if nums[i] > 0:
                # finish iteration
                break
            # if the first element or the neighboring element is not the same
            if i == 0 or nums[i - 1] != nums[i]:
                # invoke the twoPointer function
                self.twoSum(nums, i, res)
        # return the answers
        return res

    def twoSum(self, nums: List[int], i: int, res: List[List[int]]):
        # get the 3 indexes (current, leftmost from the current, and the rightmost indexes)
        left = i + 1
        right = len(nums) - 1
        # loop until the indexes converge
        while left < right:
            # calculate the sum
            sum = nums[i] + nums[left] + nums[right]
            # if the sum is below zero
            if sum < 0:
                # increase the leftmost index
                left += 1
                # if the sum is above zero
            elif sum > 0:
                # decrease the rightmost index
                right -= 1
                # if the sum equals to zero
            else:
                # add the answers to the return array
                res.append([nums[i], nums[left], nums[right]])
                # reduce the range of the left and the right index
                left += 1
                right -= 1
                # loop until left element is not a duplicate of the previous element
                while left < right and nums[left - 1] == nums[left]:
                    left += 1
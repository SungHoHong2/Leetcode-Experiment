class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # set the return array that contains the elements that sum up to zero
        res = []
        # assume that the input array is already sorted
        nums.sort()
        # iterate the numbers
        for i in range(len(nums)):
            # if the input cannot produce zero
            if nums[i] > 0:
                # finish iteration
                break
            # if the first element or the neighboring element is not the same
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSum2(nums, i, res)
        return res

    def twoSum2(self, nums: List[int], i: int, res: List[List[int]]):
        # get the index from the left and the right
        lo, hi = i + 1, len(nums) - 1
        # loop until the indexes converge
        while (lo < hi):
            # calculate the sum
            sum = nums[i] + nums[lo] + nums[hi]
            # if the sum is below zero
            if sum < 0:
                # increase the leftmost index
                lo += 1
            # if the sum is above zero
            elif sum > 0:
                # decrease the rightmost index
                hi -= 1
            # if the sum equals to zero
            else:
                # add the answers to the return array
                res.append([nums[i], nums[lo], nums[hi]])
                # reduce the range of the left and the right index
                lo += 1
                hi -= 1
                # loop until left element is not a duplicate of the previous element
                while lo < hi and nums[lo] == nums[lo - 1]:
                    lo += 1
class Solution(object):
    def maxSubArray(self, nums):

        # set up the maximum sum as the first item
        max_sum = nums[0]
        # iterate the numbers
        for i in range(1, len(nums)):
            # if the number is bigger than zero
            if nums[i - 1] > 0:
                # add the current number with the previous number
                nums[i] += nums[i - 1]
            # record the maximum sum
            max_sum = max(nums[i], max_sum)
        # return the maximum sum
        return max_sum
class Solution(object):
    def maxSubArray(self, nums):
        # set up the maximum sum as the first item
        maxSum = nums[0]
        # iterate the numbers
        for i in range(1, len(nums)):
            # if the number is bigger than zero
            if nums[i-1] > 0:
                # add the current number with the previous number
                nums[i] += nums[i-1]
            # record the maximum sum
            maxSum = max(maxSum, nums[i])
        # return the maximum sum
        return maxSum
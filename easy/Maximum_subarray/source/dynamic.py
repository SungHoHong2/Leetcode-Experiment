class Solution(object):
    def maxSubArray(self, nums):
        # set the current sum and the maxsum to the first element
        currSum = maxSum = nums[0]
        # iterate through the numbers
        for i in range(1, len(nums)):
            # record the current sum of the subarray
            currSum = max(nums[i], currSum + nums[i])
            # record the maximum sum of the subarray
            maxSum = max(currSum, maxSum)
        # return the maximum sum
        return maxSum
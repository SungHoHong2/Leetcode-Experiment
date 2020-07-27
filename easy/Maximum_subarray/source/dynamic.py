class Solution(object):
    def maxSubArray(self, nums):
        # set the current sum and the maxsum to the first element
        curr_sum = max_sum = nums[0]
        # iterate through the numbers
        for i in range(1, len(nums)):
            # record the current sum of the subarray
            curr_sum = max(nums[i], curr_sum + nums[i])
            # record the maximum sum of the subarray
            max_sum = max(max_sum, curr_sum)
        # return the maximum sum
        return max_sum
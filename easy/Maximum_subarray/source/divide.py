class Solution(object):

    def crosssum(self, nums, left, right, mid):

        # if the subarray has a single item
        if left == right:
            # return the item
            return nums[left]

        # get the largest sum from middle to left
        left_sum = float("-inf")
        cross_sum = 0
        for i in range(mid, left - 1, -1):
            cross_sum += nums[i]
            left_sum = max(cross_sum, left_sum)

        # get the largest sum from middle to right
        right_sum = float("-inf")
        cross_sum = 0
        for i in range(mid + 1, right + 1):
            cross_sum += nums[i]
            right_sum = max(cross_sum, right_sum)

        # return the sum of both left and right
        return left_sum + right_sum

    def helper(self, nums, left, right):

        # if the subarray is a single item
        if left == right:
            # return the number
            return nums[left]

        # split the subarray into half
        mid = (left + right) // 2

        # run the recursive function from left to middle
        leftsum = self.helper(nums, left, mid)

        # run the recursive function from middle to right
        rightsum = self.helper(nums, mid + 1, right)

        # check the sum of the subarray starting from the middle
        crosssum = self.crosssum(nums, left, right, mid)

        # return the biggest sum from the three subarrays
        return max(leftsum, rightsum, crosssum)

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # invoke the recursive function
        return self.helper(nums, 0, len(nums) - 1)
class Solution(object):

    def crosssum(self, nums, left, right, mid):
        if left == right:
            return nums[left]
        left_sum = float("-inf")
        cross_sum = 0
        for i in range(mid, left - 1, -1):
            cross_sum += nums[i]
            left_sum = max(cross_sum, left_sum)

        right_sum = float("-inf")
        cross_sum = 0
        for i in range(mid + 1, right + 1):
            cross_sum += nums[i]
            right_sum = max(cross_sum, right_sum)

        return left_sum + right_sum

    def helper(self, nums, left, right):
        if left == right:
            return nums[left]
        mid = (left + right) // 2

        leftsum = self.helper(nums, left, mid)
        rightsum = self.helper(nums, mid + 1, right)
        crosssum = self.crosssum(nums, left, right, mid)
        return max(leftsum, rightsum, crosssum)

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.helper(nums, 0, len(nums) - 1)
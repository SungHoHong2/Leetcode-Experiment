class Solution:
    def cross_sum(self, nums, left, right, p):
        if left == right:
            return nums[left]

        left_subsum = float('-inf')
        curr_sum = 0
        for i in range(p, left - 1, -1):
            curr_sum += nums[i]
            left_subsum = max(left_subsum, curr_sum)

        right_subsum = float('-inf')
        curr_sum = 0
        for i in range(p + 1, right + 1):
            curr_sum += nums[i]
            right_subsum = max(right_subsum, curr_sum)

        return left_subsum + right_subsum

    def helper(self, nums, left, right):

        # if the left and right are the same return the integer
        if left == right:
            return nums[left]

        # divide
        p = (left + right) // 2

        # recursively run half

        # get the biggest number from the left
        left_sum = self.helper(nums, left, p)

        # get the biggest number from the right
        right_sum = self.helper(nums, p + 1, right)

        # get the biggest number from the middle
        cross_sum = self.cross_sum(nums, left, right, p)

        # compare the results from left, right, and the middle
        return max(left_sum, right_sum, cross_sum)

    def maxSubArray(self, nums: 'List[int]') -> 'int':
        return self.helper(nums, 0, len(nums) - 1)
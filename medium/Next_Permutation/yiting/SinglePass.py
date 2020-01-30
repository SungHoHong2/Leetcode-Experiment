class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        def swap(nums, p, i):
            tmp = nums[i]
            nums[i] = nums[p]
            nums[p] = tmp

        def reverse(nums, p, n):
            while p < n:
                swap(nums, p, n)
                p += 1
                n -= 1

        n = len(nums) - 1
        p = -1
        v = 0
        for i in range(n - 1, -1, -1):
            if nums[i + 1] > nums[i]:
                p = i
                v = nums[i]
                break

        if p == -1:
            nums.reverse()
            return

        for i in range(n, -1, -1):
            if nums[i] > v:
                swap(nums, p, i)
                reverse(nums, p + 1, n)
                return




class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # assume that the smallest elements are in the right
        # ex) 5 4 5 3 2 1

        i = len(nums) - 2

        # find the decrease the element
        #       |
        # ex) 5 4 5 3 2 1
        while i >= 0 and nums[i + 1] <= nums[i]:
            i -= 1

        # swap the jth element that is smaller than ith element
        #       | |
        # ex) 5 4 5 3 2 1
        #     5 5 4 3 2 1
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1

            self.swap(nums, i, j)

        # reverse the item
        # .       |
        # ex) 5 5 4 3 2 1
        # .   5 5 1 2 3 4

        self.reverse(nums, i + 1)

    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

    def reverse(self, nums, start):
        i = start
        j = len(nums) - 1

        while i < j:
            self.swap(nums, i, j)
            i += 1
            j -= 1
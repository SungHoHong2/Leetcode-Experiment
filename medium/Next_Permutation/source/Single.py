class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # searching from the rightside to find the number that decreases
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        # if the decreasing number is found
        if i >= 0:
            # find the smallest number that is bigger than the decreasing number from the rightside
            j = len(nums) - 1
            while j >= i and nums[i] >= nums[j]:
                j -= 1
                # swap the positions of the two numbers
            nums[i], nums[j] = nums[j], nums[i]
        # make the rightside the smallest number by reversing all the numbers
        i, j = i + 1, len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1


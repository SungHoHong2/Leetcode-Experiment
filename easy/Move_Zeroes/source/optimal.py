class Solution:

    def swap(self, nums, x, y):
        temp = nums[x]
        nums[x] = nums[y]
        nums[y] = temp

    def moveZeroes(self, nums: List[int]) -> None:
        lastNonZeroFoundAt = 0
        for cur in range(len(nums)):
            if nums[cur] != 0:
                self.swap(nums, lastNonZeroFoundAt, cur)
                lastNonZeroFoundAt += 1

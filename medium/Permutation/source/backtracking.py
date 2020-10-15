class Solution:
    def permute(self, nums):
        # return output
        self.output = []
        # invoke recursion and start from swapping with the first index
        self.backtrack(0, nums, len(nums))
        return self.output

    def backtrack(self, first, nums, n):
        # append the result  if all indexes are used for swapping
        if first == n:
            self.output.append(nums[:])
        # iterate all the indexes that can be swapped with the selected index
        for i in range(first, n):
            # swap the index with the selected index
            nums[first], nums[i] = nums[i], nums[first]
            # invoke the next recursion with the using the next index
            self.backtrack(first + 1, nums, n)
            # recover the swapped array to its original state
            nums[first], nums[i] = nums[i], nums[first]
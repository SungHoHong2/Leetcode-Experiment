class Solution:
    def permute(self, nums):
        # globalize the return list and the inputs
        self.nums = nums
        # return the possible permutations
        return self.backtrack(0)

    def backtrack(self, i):
        # append the result if all indexes are used for swapping
        if i == len(self.nums):
            return [self.nums[:]]
        # iterate all the indexes that can be swapped with the selected index
        ans = list()
        for j in range(i, len(self.nums)):
            # swap the index with the selected index
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
            # invoke the next recursion with the using the next index
            ans += self.backtrack(i + 1)
            # recover the swapped array to its original state
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        return ans

class Solution:
    def permute(self, nums):
        # globalize the return list and the inputs
        self.ans, self.n, self.nums = list(), len(nums), nums
        # invoke recursion and start from swapping with the first index
        self.backtrack(0)
        # return the possible permutations
        return self.ans

    def backtrack(self, first):
        # append the result if all indexes are used for swapping
        if first == self.n:
            self.ans.append(self.nums[:])
        # iterate all the indexes that can be swapped with the selected index
        for i in range(first, self.n):
            # swap the index with the selected index
            self.nums[first], self.nums[i] = self.nums[i], self.nums[first]
            # invoke the next recursion with the using the next index
            self.backtrack(first+1)
            # recover the swapped array to its original state
            self.nums[first], self.nums[i] = self.nums[i], self.nums[first]

class Solution:
    def permute(self, nums):

        # total number of length
        n = len(nums)

        # return output
        self.output = []

        # run backtrack(first=0)
        self.backtrack(0, nums, n)

        return self.output

    def backtrack(self, first, nums, n):
        # if all integers are used up
        if first == n:
            self.output.append(nums[:])

        for i in range(first, n):
            # place i-th integer first

            # swap with first item
            nums[first], nums[i] = nums[i], nums[first]
            # first = 0, i = 1
            # [0,1,2] -> [1,0,2]

            # use next integers to complete the permutations
            self.backtrack(first + 1, nums, n)

            # backtrack (reverse to original state)
            nums[first], nums[i] = nums[i], nums[first]
            # first = 0, i = 1
            # [1,0,2] -> [0,1,2]



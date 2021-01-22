class Solution:
    def firstMissingPositive(self, nums):
        # get the largest number possible in the input
        n = len(nums)
        # return 1 if the input does not contain 1
        if 1 not in nums:
            return 1
        # return 2 if the input only contains 1
        if n == 1:
            return 2
        # create a hashmap that checks the possible numbers
        hashmap = {i:False for i in range(1, n+1) }
        # collect the numbers that are not negative numbers, zeros, and numbers larger than n
        for i in range(n):
            if not(nums[i] <= 0 or nums[i] > n):
                hashmap[nums[i]] = True
        # return the missing number if exists
        for key, value in hashmap.items():
            if not value:
                return key
        # return the n + 1 if all number exists
        return n + 1
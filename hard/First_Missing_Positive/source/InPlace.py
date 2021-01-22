class Solution:
    def firstMissingPositive(self, nums):
        # get the largest number
        n = len(nums)
        # return 1 if the input does not contain 1
        if 1 not in nums:
            return 1
        # Suppose that there is 1 in the input return 2 if the length of the input is 1
        if n == 1:
            return 2
        # Replace negative numbers, zeros, and numbers larger than n by 1s (since 1 already exists).
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1
        # Use index as a hash key and number sign as a presence detector
        for i in range(n):
            # get the value to use as an index (consider that the value is continuously updated)
            a = abs(nums[i])
            # mark the largest number(n) as exist(negative)
            if a == n:
                nums[0] = - abs(nums[0])
            # mark the number between 1 and n as exist(negative)
            else:
                nums[a] = - abs(nums[a])
        # return the missing number(positive) if exists
        for i in range(1, n):
            if nums[i] > 0:
                return i
        # return n if only the last number is missing
        if nums[0] > 0:
            return n
        # return the n + 1 if all number exists
        return n + 1
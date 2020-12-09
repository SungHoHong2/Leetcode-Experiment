class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # get the length of the input
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

        # Use index as a hash key and number sign as a presence detector.
        for i in range(n):
            # get the value to use as an index
            a = abs(nums[i])
            # update the value of the first index (knowing that 0 no longer exist) if the index equals to n
            if a == n:
                nums[0] = - abs(nums[0])
            # update the value of the index
            else:
                nums[a] = - abs(nums[a])

        # return the first positive number found in the value of the index
        for i in range(1, n):
            if nums[i] > 0:
                return i

        # return n if the first index is positive
        if nums[0] > 0:
            return n

        # return the n + 1 if all number from 1 to n exists in the input
        return n + 1
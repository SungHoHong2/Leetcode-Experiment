class Solution(object):
    def valid(self, nums, m, pivot):
        # set the number of subsets and the current accumulated value
        subsets, curr = 1, 0
        # iterate the input
        for num in nums:
            # accumulate the sum
            curr += num
            # if the sum exceeds the pivot
            if curr > pivot:
                # create a subset
                subsets += 1
                # start the new accumulated value
                curr = num
                # return if the number of subsets are acceptable
        return subsets <= m

    def splitArray(self, nums, m):
        # get the smallest and largest possible value with a single subset
        left, right = max(nums), sum(nums)
        # set the returning value that records the smallest maximum value of the subset
        ans = float('-inf')
        # run binary search until low and high coverges
        while left <= right:
            # get the pivot
            pivot = (left + right) // 2
            # update the answer and explore the smaller possible values
            if self.valid(nums, m, pivot):
                ans, right = pivot, pivot - 1
            # explore right if the the subsets are invalid
            else:
                left = pivot + 1
                # return the smallest maximum value of the subset
        return ans
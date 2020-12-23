class Solution(object):
    def is_valid(self, nums, m, mid):
        # count the number of subsets that has the value within the pivot
        cuts, curr_sum = 0, 0
        for x in nums:
            curr_sum += x
            if curr_sum > mid:
                cuts, curr_sum = cuts + 1, x
        subs = cuts + 1
        # return true if the number of subsets is valid
        return (subs <= m)

    def splitArray(self, nums, m):
        # set the smallest value of the subset as the low and the largest as the right
        low, high = max(nums), sum(nums)
        # set the returning value that records the smallest maximum value of the subset
        ans = float('-inf')
        # run binary search until low and high coverges
        while low <= high:
            # get the pivot
            mid = (low + high) // 2
            # update the answer and explore left if the subsets are valid
            if self.is_valid(nums, m, mid):
                ans, high = mid, mid - 1
            # explore right if the the subsets are invalid
            else:
                low = mid + 1
        # return the smallest maximum value of the subset
        return ans
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # reframe the problem
        nums = [1] + nums + [1]
        # set a cache
        memo = dict()
        def dp(left, right):
            # no more balloons can be added
            if left + 1 == right: return 0
            # return the cached results if already explored
            if (left,right) in memo:
                return memo[(left,right)]
            # add each balloon on the interval and return the maximum score
            memo[(left,right)] = max(nums[left] * nums[i] * nums[right] + dp(left, i) + dp(i, right) for i in range(left+1, right))
            return memo[(left,right)]
        # find the maximum number of coins obtained from adding all balloons
        return dp(0, len(nums)-1)
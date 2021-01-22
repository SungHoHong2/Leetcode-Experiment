class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # reframe the input
        nums = [1] + nums + [1]
        # set a cache
        dp = dict()
        def topdown(left, right):
            # no more balloons left to pop
            if left + 1 == right: return 0
            # return the cached results if already explored
            if (left,right) in dp:
                return dp[(left,right)]
            # collect the maximum score of popping the three balloons within the range between left and right
            score = 0
            for i in range(left+1, right):
                score = max(score, nums[left] * nums[i] * nums[right] + topdown(left, i) + topdown(i, right))
            # record the answer to the dp
            dp[(left,right)] = score
            # return the highest score
            return dp[(left,right)]
        # find the maximum number of coins obtained from adding all balloons
        return topdown(0, len(nums)-1)
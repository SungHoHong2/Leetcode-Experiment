class Solution:
    def jump(self, nums: List[int]) -> int:
        # return 0 if there is only one item in the input
        if len(nums) == 1:
            return 0
            # get the destination
        destination = len(nums) - 1
        # set a variable to record the valid coverage and the index of the last jump
        coverage, furthestJump = 0, 0
        # set a counter for the number of jumps
        jumps = 0
        # apply greedy strategy that finds the largest coverage
        for i in range(0, len(nums)):
            # record the furthest possible jump
            coverage = max(coverage, i + nums[i])
            # the current position equals to the furthest jump
            if i == furthestJump:
                # update last jump index
                furthestJump = coverage
                # update counter of jump by +1
                jumps += 1
                # return the number of jumps once the current coverage covers the destination
                if coverage >= destination:
                    return jumps


class Solution:
    def trap(self, height: List[int]) -> int:
        # return zero if there is no input
        if not height:
            return 0
        # set the table for the maximum height of left and right
        left_max, right_max = [0 for _ in range(len(height))], [0 for _ in range(len(height))]
        # record the maximum height from the left
        left_max[0] = height[0]
        for i in range(1, len(height)):
            left_max[i] = max(height[i],left_max[i-1])
        # record the maximum height from the right
        right_max[-1] = height[-1]
        for i in range(len(height)-2, -1, -1):
            right_max[i] = max(height[i], right_max[i+1])
        # accumulate the available space for each of the x-axis
        ans = 0
        for i in range(1, len(height)):
            ans += min(left_max[i], right_max[i]) - height[i]
        # return the total available space for the rain water
        return ans
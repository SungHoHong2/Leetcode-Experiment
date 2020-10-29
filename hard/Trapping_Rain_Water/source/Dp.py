class Solution:
    def trap(self, height: List[int]) -> int:
        # return zero if there is no input
        if not height:
            return 0
        # get the size of the input
        size = len(height)
        # set the table for the maximum height of left and right
        leftMax, rightMax = [0 for i in range(size)], [0 for i in range(size)]
        # record the maximum height from the left
        leftMax[0] = height[0]
        for i in range(1,size):
            leftMax[i] = max(height[i], leftMax[i-1])
        # record the maximum height from the right
        rightMax[size-1] = height[size-1]
        for i in range(size-2,-1,-1):
            rightMax[i] = max(height[i], rightMax[i+1])
        # get the minimum height from both left and right and get the available space
        ans = 0
        for i in range(1, size):
            ans += min(leftMax[i], rightMax[i])-height[i]
        # return the total available space for the rain water
        return ans
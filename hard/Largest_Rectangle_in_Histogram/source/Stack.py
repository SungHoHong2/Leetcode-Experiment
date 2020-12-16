class Solution:
    def largestRectangleArea(self, height):
        # height append 0 in case there is no input
        height.append(0)
        # set a stack that will never be empty
        stack = [-1]
        # set the returning answer
        ans = 0
        # iterate the input
        for i in range(len(height)):
            # if the current height is smaller than the head of the stack
            while height[i] < height[stack[-1]]:
                # get the hieght
                h = height[stack.pop()]
                # get the widith
                w = i - stack[-1] - 1
                # record the maximum area
                ans = max(ans, h * w)
            # add the height
            stack.append(i)
        # return the largest area
        return ans


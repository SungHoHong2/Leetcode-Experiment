class Solution:
    def trap(self, height: List[int]) -> int:
        # set the answer
        ans = 0
        # set the stack
        stack = list()
        # iterate the heights
        for i in range(len(height)):
            # loop the stack until a hole is detected
            while stack and height[stack[-1]] < height[i]:
                # pop the height that serves as the bottom from the stack
                bottom = height[stack.pop()]
                # finish the loop if there are no more left heights to compute area
                if not stack:
                    break
                # calculate the distance
                x = i - stack[-1] - 1
                # get the left height from the stack
                left = height[stack[-1]]
                # get the right height
                right = height[i]
                # calculate the available height
                y = min(left, right) - bottom
                # aggregate the available space for the rain
                ans += x * y
            # append the previous heights in the stack
            stack.append(i)
        # return the available space fore the rain
        return ans
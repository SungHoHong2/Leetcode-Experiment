class Solution:
    def largestRectangleArea(self, height):
        # create a stack with -1 to calculate the area for first rectangle
        stack = [-1]
        # set the returning answer
        ans = 0
        # iterate the input
        for i in range(len(height)):
            # if the current height is smaller than the head of the stack
            while height[i] < height[stack[-1]]:
                # get the height
                h = height[stack.pop()]
                # get the width
                w = i - stack[-1] - 1
                # record the maximum area
                ans = max(ans, h * w)
            # add the height
            stack.append(i)
        # return the largest area
        return ans

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # return 0 if there is no input
        if not matrix:
            return 0
        # set a variable for recording the maximum area
        maxarea = 0
        # set up a dp table
        dp = [0 for _ in range(len(matrix[0]))]
        # append -1 to calculate the area of the first height
        dp.append(-1)
        # iterate the row of the matrix
        for i in range(len(matrix)):
            # iterate the col of the matrix
            for j in range(len(matrix[0])):
                # accumulate the maximum height from the previous row
                dp[j] = dp[j] + 1 if matrix[i][j] == '1' else 0
            # calculate the maximum area using stack
            maxarea = max(maxarea, self.largestRectangleArea(dp))
        # return the maximum area
        return maxarea
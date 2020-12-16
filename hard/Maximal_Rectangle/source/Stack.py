class Solution:
    # Get the maximum area in a histogram given its heights
    def leetcode84(self, height):
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

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # return 0 if there is no input
        if not matrix: return 0
        # set a variable for recording the maximum area
        maxarea = 0
        # set up a dp table
        dp = [0] * len(matrix[0])
        # iterate the row of the matrix
        for i in range(len(matrix)):
            # iterate the col of the matrix
            for j in range(len(matrix[0])):
                # accumulate the maximum width from the previous row
                dp[j] = dp[j] + 1 if matrix[i][j] == '1' else 0
            # update maxarea
            maxarea = max(maxarea, self.leetcode84(dp))
        return maxarea
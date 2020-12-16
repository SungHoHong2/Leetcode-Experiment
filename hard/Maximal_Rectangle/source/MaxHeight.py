class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # return 0 if there is no input
        if not matrix: return 0
        # get the length of the rows
        m = len(matrix)
        # get the length of the columns
        n = len(matrix[0])
        # set the dp table for left, right, height
        left = [0] * n
        right = [n] * n
        height = [0] * n
        # set the variable for recording the maximum area
        maxarea = 0
        # iterate the row of the input
        for i in range(m):
            # set the current left and right
            cur_left, cur_right = 0, n
            # update height
            for j in range(n):
                if matrix[i][j] == '1': height[j] += 1
                else: height[j] = 0
            # update left
            for j in range(n):
                if matrix[i][j] == '1': left[j] = max(left[j], cur_left)
                else:
                    left[j] = 0
                    cur_left = j + 1
            # update right
            for j in range(n-1, -1, -1):
                if matrix[i][j] == '1': right[j] = min(right[j], cur_right)
                else:
                    right[j] = n
                    cur_right = j
            # update the area
            for j in range(n):
                maxarea = max(maxarea, height[j] * (right[j] - left[j]))
        # return the maximum area
        return maxarea

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # return 0 if there is no input
        if not matrix:
            return 0
        # get the length of the rows
        m = len(matrix)
        # get the length of the columns
        n = len(matrix[0])
        # set the dp table for left, right, height
        left, right, height = [0 for _ in range(n)], [n for _ in range(n)], [0 for _ in range(n)]
        # set the variable for recording the maximum area
        maxarea = 0
        # iterate the row of the input
        for i in range(m):
            # set the current left and right
            cur_left, cur_right = 0, n
            # accumulate the height for each columns or set as invalid
            for j in range(n):
                height[j] = (height[j] + 1) if matrix[i][j] == '1' else False
            # update the available left index
            for j in range(n):
                # maintain the maximum width if the height is valid
                if height[j]:
                    left[j] = max(left[j], cur_left)
                # reduce the maximum width if the height is invalid
                else:
                    left[j] = 0
                    cur_left = j + 1
            # update the available right index
            for j in range(n-1, -1, -1):
                # maintain the maximum width if the height is valid
                if height[j]:
                    right[j] = min(right[j], cur_right)
                # reduce the maximum width if the height is invalid
                else:
                    right[j] = n
                    cur_right = j
            # update the area
            for j in range(n):
                # compute the area if the height is valid
                if height[j]:
                    maxarea = max(maxarea, height[j] * (right[j] - left[j]))
        # return the maximum area
        return maxarea
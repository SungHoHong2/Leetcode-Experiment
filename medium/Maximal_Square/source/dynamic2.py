class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # return 0 if there is no matrix
        if not matrix:
            return 0
        # get the length of the rows
        rows = len(matrix)
        # get the length of the columns
        cols = len(matrix[0])
        # reduce the original table to a single row
        dp = [0 for i in range(cols + 1)]
        # set the variable for tracking the maximum length
        maxqlen = 0
        # set the variable to track the diagonal
        diagonal = 0
        # iterate the rows
        for i in range(1, rows + 1):
            # iterate the cols
            for j in range(1, cols + 1):
                # get the top
                top = dp[j]
                # if the current cell is 1
                if matrix[i - 1][j - 1] == '1':
                    # get the left
                    left = dp[j - 1]
                    # update the maximum size of the square
                    dp[j] = min(left, diagonal, top) + 1
                    # keep track of the maximum length of the square
                    maxqlen = max(maxqlen, dp[j])
                # update the current maximum size of the square to zero
                else:
                    dp[j] = 0
                # get the diagonal
                diagonal = top
        # return the size of the maximum square
        return pow(maxqlen, 2)
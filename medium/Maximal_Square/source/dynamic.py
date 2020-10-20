class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # return 0 if there is no input
        if not matrix:
            return 0
        # get the length of the rows
        rows = len(matrix)
        # get the length of the columns
        cols = len(matrix[0])
        # create a table for storing the results of the subproblems
        dp = [[0 for i in range(cols + 1)] for j in range(rows + 1)]
        # set the integer to record the maximum length
        maxqlen = 0
        # iterate the rows
        for i in range(1, rows + 1):
            # iterate the cols
            for j in range(1, cols + 1):
                # if the current cell is "1"
                if matrix[i - 1][j - 1] == '1':
                    # increment from the left, top, and diagonal results
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
                    # keep track of the maximum length of the square
                    maxqlen = max(maxqlen, dp[i][j])
        # return the size of the maximum square
        return pow(maxqlen, 2)
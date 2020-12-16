class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # set the variable to record the maximum area
        maxarea = 0
        # set a dp table
        dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        # iterate the row of the dp table
        for i in range(len(matrix)):
            # iterate the col of the dp table
            for j in range(len(matrix[0])):
                # continue if the area is not valid
                if matrix[i][j] == '0': continue
                # compute the maximum width to convert the input into a set of histograms
                width = dp[i][j] = dp[i][j-1] + 1 if j else 1
                # compute the maximum area rectangle from the precomputed rows
                for k in range(i, -1, -1):
                    width = min(width, dp[k][j])
                    maxarea = max(maxarea, width * (i-k+1))
        return maxarea
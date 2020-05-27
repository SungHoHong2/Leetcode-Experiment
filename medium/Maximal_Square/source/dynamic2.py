class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        if not matrix:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])

        dp = [0 for i in range(cols + 1)]

        maxqlen = 0
        prev = 0

        for i in range(1, rows + 1):
            for j in range(1, cols + 1):

                # use temp as previous
                temp = dp[j]

                if matrix[i - 1][j - 1] == '1':

                    #
                    dp[j] = min(dp[j - 1], prev, dp[j]) + 1
                    maxqlen = max(maxqlen, dp[j])
                else:
                    dp[j] = 0

                prev = temp

        return pow(maxqlen, 2)



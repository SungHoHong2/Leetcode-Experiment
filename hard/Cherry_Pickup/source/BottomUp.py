class Solution(object):

    def cherryPickup(self, grid):
        # get the total length of the grid (row == col)
        N = len(grid)
        # set the 2D table
        dp = [[float('-inf')] * N for _ in range(N)]
        # start from the beginning
        dp[0][0] = grid[0][0]
        # explore all the cells
        for t in range(1, 2 * N - 1):
            # set the temporary dp table
            dp2 = [[float('-inf')] * N for _ in range(N)]
            # explore all possible directions of the two persons for each step
            start = max(0, t - (N - 1))
            end = min(N - 1, t) + 1
            for i in range(start, end):
                for j in range(start, end):
                    # if one of the person meet a thorn
                    if grid[i][t - i] == -1 or grid[j][t - j] == -1:
                        continue
                    # collect the cherry from the first person
                    val = grid[i][t - i]
                    # add the second person if the he explored different location
                    if i != j: val += grid[j][t - j]
                    # accumulate the result from the 'concluded' dp table
                    # note that before completing the first half of the dp table, there is an unncessary update)
                    dp2[i][j] = max(dp[pi][pj] + val for pi in (i - 1, i) for pj in (j - 1, j) if pi >= 0 and pj >= 0)
            # conclude the dp table
            dp = dp2
        # return the total collected cherries from the dp table
        return max(0, dp[N - 1][N - 1])
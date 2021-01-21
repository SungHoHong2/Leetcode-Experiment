class Solution(object):

    def cherryPickup(self, grid):
        # get the total length of the grid (row == col)
        N = len(grid)
        # set the 2D table
        dp = [[float('-inf')] * N for _ in range(N)]
        # start from the beginning
        dp[0][0] = grid[0][0]
        # iterate all the layers
        for t in range(1, 2 * N - 1):
            # set the temporary dp table
            dp2 = [[float('-inf')] * N for _ in range(N)]
            # the start of the layer increases after it moves beyond the half
            start = max(0, t - (N - 1))
            # the end of the layer stops increasing after it moves beyond the half
            end = min(N - 1, t) + 1
            # iterate the current layer
            for i in range(start, end):
                for j in range(start, end):
                    # if one of the person meet a thorn
                    if grid[i][t - i] == -1 or grid[j][t - j] == -1:
                        continue
                    # collect the cherry from the first person
                    val = grid[i][t - i]
                    # add the second person if the he explored different location
                    if i != j: val += grid[j][t - j]
                    # accumulate the dp table from the dp table made from the previous layer
                    dp2[i][j] = max(dp[pi][pj] + val for pi in (i - 1, i) for pj in (j - 1, j) if pi >= 0 and pj >= 0)
            # save the state of the dp table
            dp = dp2
        # return the total collected cherries from the dp table
        return max(0, dp[N - 1][N - 1])
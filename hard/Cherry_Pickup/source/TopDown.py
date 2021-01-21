class Solution(object):
    def topdown(self, grid, r1, c1, c2):
        # calculate the r2
        r2 = r1 + c1 - c2
        # get the total length of the grid
        N = len(grid)
        # return infinite if the index exceeds or have the thorns
        if not(r1 < N and r2 < N and c1 < N and c2 < N) or grid[r1][c1] == -1 or grid[r2][c2] == -1:
            return float('-inf')
        # return the result if one person reached the destination
        elif r1 == c1 == N - 1:
            return grid[r1][c1]
        # return the recorded result if exists
        elif self.dp[r1][c1][c2] is not None:
            return self.dp[r1][c1][c2]
        # if index is the unexplored area
        else:
            # pick the cherry from one person and the second person if it is not the same
            ans = grid[r1][c1] + (c1 != c2) * grid[r2][c2]
            # recursively collect the maximum result
            ans += max(self.topdown(grid, r1, c1 + 1, c2 + 1), self.topdown(grid, r1 + 1, c1, c2 + 1),
                       self.topdown(grid, r1, c1 + 1, c2), self.topdown(grid, r1 + 1, c1, c2))
            # record the visited area
            self.dp[r1][c1][c2] = ans
            # return the total number of picked cherries
            return ans

    def cherryPickup(self, grid):
        # initiate the table for dp[r1][c1][c2]
        self.dp = [[[None for _ in range(len(grid))] for _ in range(len(grid))] for _ in range(len(grid))]
        # return the result of the recursive function
        return max(0, self.topdown(grid, 0, 0, 0))

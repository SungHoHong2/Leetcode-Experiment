class Solution(object):

    def dp(self, grid, r1, c1, c2):
        # calculate the r2
        r2 = r1 + c1 - c2
        # set the total length
        N = len(grid)
        # return infinite if the row and columns of the two person reach the limit or meet the thorns
        if (N == r1 or N == r2 or N == c1 or N == c2 or
                grid[r1][c1] == -1 or grid[r2][c2] == -1):
            return float('-inf')
        # return the result if one person reached the destination
        elif r1 == c1 == N - 1:
            return grid[r1][c1]
        # use memoization if it is visited area
        elif self.memo[r1][c1][c2] is not None:
            return self.memo[r1][c1][c2]
        # if it is the unexplored area
        else:
            # pick the cherry from one person and the second person if it is not the same
            ans = grid[r1][c1] + (c1 != c2) * grid[r2][c2]
            # recursively collect the maximum result
            ans += max(self.dp(grid, r1, c1 + 1, c2 + 1), self.dp(grid, r1 + 1, c1, c2 + 1),
                       self.dp(grid, r1, c1 + 1, c2), self.dp(grid, r1 + 1, c1, c2))
        # use memoization to store the visited area
        self.memo[r1][c1][c2] = ans
        return ans

    def cherryPickup(self, grid):
        # initiate the table for dp[r1][c1][c2]
        self.memo = [[[None] * len(grid) for _1 in range(len(grid))] for _2 in range(len(grid))]
        # return the result of the recursive function
        return max(0, self.dp(grid, 0, 0, 0))
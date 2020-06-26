class Solution:

    def dfs(self, grid, r, c):

        # return if the table is zero or the table is out of range
        if not (0 <= r < self.nr) or not (0 <= c < self.nc) or grid[r][c] == '0':
            return

            # mark the viewed table as zero
        grid[r][c] = '0'

        # search through all the table recursively
        self.dfs(grid, r - 1, c)
        self.dfs(grid, r + 1, c)
        self.dfs(grid, r, c - 1)
        self.dfs(grid, r, c + 1)

    def numIslands(self, grid: List[List[str]]) -> int:

        # if the grid has nothing return 0
        if len(grid) == 0:
            return 0

        # set the number of rows and cols
        self.nr = len(grid)
        self.nc = len(grid[0])

        # initialize the total number of islands
        num_islands = 0

        # iterate the cells of the table
        for r in range(0, self.nr):
            for c in range(0, self.nc):

                # if there is a ground
                if grid[r][c] == '1':
                    # add one island
                    num_islands += 1
                    # execute the recursive depth-first-search
                    self.dfs(grid, r, c)

        return num_islands
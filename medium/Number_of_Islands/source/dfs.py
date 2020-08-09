class Solution:

    def dfs(self, grid, r, c):
        # return if the table is viewed, water, or out of range
        if not (0 <= r < len(grid)) or not (0 <= c < len(grid[0])) or grid[r][c] == '0':
            return
        # mark index as viewed
        grid[r][c] = '0'
        # search through all the table recursively
        self.dfs(grid, r - 1, c)
        self.dfs(grid, r + 1, c)
        self.dfs(grid, r, c - 1)
        self.dfs(grid, r, c + 1)

    def numIslands(self, grid: List[List[str]]) -> int:

        # if the grid has nothing return 0
        if not grid:
            return 0
        # initialize the total number of islands
        total = 0
        # iterate the cells of the table
        for r in range(0, len(grid)):
            for c in range(0, len(grid[0])):
                # if there is a ground
                if grid[r][c] == '1':
                    # add one island
                    total += 1
                    # execute the recursive depth-first-search
                    self.dfs(grid, r, c)
        # return the number of islands
        return total
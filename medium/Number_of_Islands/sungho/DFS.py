# Linear scan the 2d grid map,
# if a node contains a '1', then it is a root node that triggers a Depth First Search
# During DFS, every visited node should be set as '0' to mark as visited node.
# Count the number of root nodes that trigger DFS
# this number would be the number of islands since each DFS starting at some root identifies an island.

class Solution:

    def dfs(self, grid, r, c):
        nr = len(grid)
        nc = len(grid[0])

        if r < 0 or c < 0 or r >= nr or c >= nc or grid[r][c] == '0':
            return

        grid[r][c] = '0'
        self.dfs(grid, r - 1, c)
        self.dfs(grid, r + 1, c)
        self.dfs(grid, r, c - 1)
        self.dfs(grid, r, c + 1)

    def numIslands(self, grid: List[List[str]]) -> int:

        for i in grid:
            print(i)

        if grid == None or len(grid) == 0:
            return 0

        # get the number of rows
        nr = len(grid)

        # get the number of columns
        nc = len(grid[0])
        num_islands = 0

        for r in range(0, nr):
            for c in range(0, nc):
                if grid[r][c] == '1':
                    num_islands += 1
                    self.dfs(grid, r, c)

        return num_islands



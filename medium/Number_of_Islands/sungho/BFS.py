class Solution:

    def numIslands(self, grid):

        if not grid:
            return 0

        row, col = len(grid), len(grid[0])

        # find all the row and column indexes that have the number "1"
        # (row,col) == 1

        s = set([(i, j) for i in range(0, row) for j in range(0, col) if grid[i][j] == '1'])
        num = 0

        # empty all the set that hve the number "1"
        while s:
            num += 1
            queue = []
            queue.append(s.pop())

            while len(queue) > 0:

                # get the (row,col) that contains the number "1"
                i, j = queue.pop()

                # empty the neighbors of the (row,col) that are in the set
                for item in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                    if item in s:
                        s.remove(item)
                        queue.append(item)

        return num

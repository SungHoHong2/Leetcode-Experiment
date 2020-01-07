class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        s = set((i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == '1')
        c = 0
        queue = []
        while s:
            c += 1
            queue.append(s.pop())
            while len(queue) > 0:
                i, j = queue.pop()
                for item in [(i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)]:
                    if item in s:
                        s.remove(item)
                        queue.append(item)

        return c

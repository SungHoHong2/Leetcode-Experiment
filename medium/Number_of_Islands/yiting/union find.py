class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        def getRank(p):
            i, j = p
            return rank[i][j]

        def setRank(p, r):
            i, j = p
            rank[i][j] = r

        def setParent(p, q):
            i, j = p
            parent[i][j] = q

        def find(p):
            i, j = p
            x, y = i, j

            while parent[x][y] != (x, y):
                x, y = parent[x][y]
            parent[i][j] = parent[x][y]
            return parent[i][j]

        def union(p, q):
            p1 = find(p)
            p2 = find(q)

            r1 = getRank(p)
            r2 = getRank(q)
            if r1 > r2:
                setParent(p2, p1)
            elif r1 < r2:
                setParent(p1, p2)
            else:
                setParent(p2, p1)
                setRank(p1, r1 + r2)

        parent = [[(i, j) for j in range(len(grid[0]))] for i in range(len(grid))]
        rank = [[1 for i in range(len(grid[0]))] for j in range(len(grid))]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    for x, y in [(i + 1, j), (i, j + 1)]:
                        if x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0]) and grid[x][y] == '1':
                            union((i, j), (x, y))

        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and find((i, j)) == (i, j):
                    result += 1

        return result


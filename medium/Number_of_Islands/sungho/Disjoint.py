class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0

        N, M = len(grid), len(grid[0])

        # table of indexes (row, col)
        parent = [[(i, j) for j in range(M)] for i in range(N)]

        # set the table of ranking to 1
        rank = [[1 for i in range(M)] for j in range(N)]

        # set the representative of the grouped elements
        def setParent(x, p):
            i, j = x
            parent[i][j] = p

        # rank = the number of the grouped elements
        def getRank(p):
            x, y = p
            return rank[x][y]

        def setRank(p, r):
            x, y = p
            rank[x][y] = r

        # find the parent of the node
        def find(p):
            # get the index of the node
            i, j = p
            x, y = i, j

            # if the node is not the parent
            while parent[x][y] != (x, y):
                # get the index of the parent
                x, y = parent[x][y]

            # update the parent table of that node
            parent[i][j] = parent[x][y]

            # return the index of the parent
            return parent[i][j]

        def union(a, b):
            # get the parents of both 'a' and 'b'
            p_a, p_b = find(a), find(b)

            # return the ranks of both 'a' and 'b'
            rank_a, rank_b = getRank(p_a), getRank(p_b)

            # if the rank of the 'b' is higher
            if rank_a < rank_b:
                # set the parent of 'a' to parent of 'b'
                setParent(p_a, p_b)

            elif rank_b < rank_a:
                setParent(p_b, p_a)

            # if the ranks of 'a' and 'b' are the same
            else:
                setParent(p_b, p_a)
                # increase the number of rank and merge the group
                setRank(p_a, rank_a + 1)

        # row +1 or col + 1
        directions = [(1, 0), (0, 1)]

        for i in range(N):
            for j in range(M):
                if grid[i][j] == '1':
                    for di, dj in directions:
                        ni, nj = i + di, j + dj

                        # merge all the (row,col) that contains "1"
                        if 0 <= ni < N and 0 <= nj < M and grid[ni][nj] == '1':
                            union((i, j), (ni, nj))
        count = 0
        for i in range(N):
            for j in range(M):

                # count the total number grouped elements
                if grid[i][j] == '1' and find((i, j)) == (i, j):
                    count += 1

        # return the number of the group
        return count
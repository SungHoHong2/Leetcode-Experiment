class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0


        row, col = len(grid), len(grid[0])

        # table of indexes Note:(row, col)
        parent = [[(i, j) for j in range(col)] for i in range(row)]

        # set the table of ranking to 1
        rank = [[1 for i in range(col)] for j in range(row)]

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
            if parent[x][y] != (x, y):
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

        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    for di, dj in [(i+1,j),(i,j+1)]:
                        # merge all the (row,col) that contains "1"
                        if 0 <= di < row and 0 <= dj < col and grid[di][dj] == '1':
                            union((i, j), (di, dj))
        count = 0
        for i in range(row):
            for j in range(col):

                # count the total number grouped elements
                if grid[i][j] == '1' and find((i, j)) == (i, j):
                    count += 1

        # return the number of the group
        return count
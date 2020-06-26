class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # if grid is not valid
        if not grid:
            return 0

            # get the length of the row and the col of the grid
        row, col = len(grid), len(grid[0])

        # Disjoint Set BEGIN
        # initialize the parent table
        parents = [[(r, c) for c in range(col)] for r in range(row)]

        # set the ranking table
        ranking = [[1 for c in range(col)] for r in range(row)]

        # set parent of the cell
        def setParent(curr, parent):
            # get the address of the current cell
            x, y = curr

            # store the parent address to the current cell
            parents[x][y] = parent

        # return the rank of the parent
        def getRank(parent):
            # get the address of the parent
            x, y = parent

            # return the rank from the table
            return ranking[x][y]

        # update the rank of the parent
        def setRank(parent, rank):
            # get the address of the parent
            x, y = parent

            # update the rank
            ranking[x][y] = rank

            # find the parent of the node

        def find(current):
            # get the index of the node
            x, y = current
            # set the temporary pointer just in case the current node already has a parent
            i, j = x, y

            # if the selected node already has a parent (node != parent)
            if parents[i][j] != current:
                # get the address of the parent
                i, j = parents[i][j]

            # update the parent table of that node
            parents[x][y] = parents[i][j]

            # return the index of the parent
            return parents[x][y]

        def union(a, b):
            # get the parents of both 'a' and 'b'
            p_a, p_b = find(a), find(b)

            # return the ranks of both 'a' and 'b'
            rank_a, rank_b = getRank(p_a), getRank(p_b)

            # if the rank of the 'b' is higher
            if rank_a < rank_b:
                # set the parent of 'a' to parent of 'b'
                setParent(p_a, p_b)

            # if the rank of the 'a' is higher
            elif rank_a > rank_b:
                # set the parent of 'b' to parent of 'a'
                setParent(p_b, p_a)

            # if the ranks of 'a' and 'b' are the same
            else:
                # increase the number of rank and merge the group
                setParent(p_b, p_a)
                setRank(p_a, rank_a + 1)

        # Disjoint Set END

        # iterate the grid
        for i in range(row):
            for j in range(col):
                # if the cell is the ground
                if grid[i][j] == '1':
                    # get the right and bottom cells
                    for item in [(i + 1, j), (i, j + 1)]:
                        # merge all the (row,col) that contains "1"
                        r, c = item
                        if (0 <= r < row) and (0 <= c < col) and grid[r][c] == '1':
                            union((i, j), (r, c))

        # initialize the total number of islands
        totalIslands = 0

        # iterate the grid
        for i in range(row):
            for j in range(col):
                # if it is a ground and is the parent
                if grid[i][j] == '1' and find((i, j)) == (i, j):
                    # increase the number of islands
                    totalIslands += 1

                    # return the number of islands
        return totalIslands

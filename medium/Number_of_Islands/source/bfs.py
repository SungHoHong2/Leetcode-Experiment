class Solution:

    def numIslands(self, grid):

        # if there is not grid return 0
        if not grid:
            return 0

            # init the total number of islands
        totalIslands = 0

        # get the total length of the row and the col
        nr, nc = len(grid), len(grid[0])

        # create a set that contains the address of the cells containig value "1"
        grounds = set((i, j) for i in range(nr) for j in range(nc) if grid[i][j] == '1')

        # iterate the set until the set is empty
        while grounds:

            # increase the number of total islands
            totalIslands += 1

            # init a queue
            queue = []

            # pop one island from the set to the queue
            queue.append(grounds.pop())

            # iterate until the queue is empty
            while queue:

                # pop one island from the queue
                r, c = queue.pop()

                # empty the neighbors of the (row,col) that are in the set
                for neighbor in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:

                    # if the neighbors are part of the set
                    if neighbor in grounds:
                        # remove the neighbor from the set
                        grounds.remove(neighbor)

                        # add the neighhbor to the queue
                        queue.append(neighbor)

        # return the final result
        return totalIslands

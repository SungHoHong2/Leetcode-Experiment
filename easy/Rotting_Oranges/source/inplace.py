class Solution(object):
    def orangesRotting(self, grid):
        # set the total length of rows and cols of the grid
        ROWS, COLS = len(grid), len(grid[0])
        # set the variables for directions
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        # set the variable that is used both as verifying the rotten oranges and the time
        timestamp = 2
        # set the flag that is used to stop the loop
        to_be_continued = True
        # iterate until meets flag is set to stop
        while to_be_continued:
            to_be_continued = False
            # iterate through the grid
            for row in range(ROWS):
                for col in range(COLS):
                    # if the orange is a rotten
                    if grid[row][col] == timestamp:
                        # check the neighbors
                        for d in directions:
                            n_row, n_col = row + d[0], col + d[1]
                            # if the row and columns are within the grid
                            if ROWS > n_row >= 0 and COLS > n_col >= 0:
                                # i the orange is fresh
                                if grid[n_row][n_col] == 1:
                                    # increase the number of timestamp indicating the orange as the rotten
                                    grid[n_row][n_col] = timestamp + 1
                                    # set the flag to loop again
                                    to_be_continued = True

                                    # if the rotten orange is found and needs to continue
            if to_be_continued:
                # increase the timestamp
                timestamp += 1

                # end of process, to check if there are still fresh oranges left
        # iterate through the grid
        for row in grid:
            for cell in row:
                # still got a fresh orange left
                if cell == 1:
                    # return -1
                    return -1
        # return elapsed minutes if no fresh orange left
        return timestamp - 2
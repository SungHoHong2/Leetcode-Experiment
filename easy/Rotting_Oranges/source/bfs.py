class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # set the number of fresh oranges
        fresh_oranges = 0
        # create a deque with rotten oranges by iterating through the grid
        queue = collections.deque()
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_oranges += 1
        # used as a flag to check teh number of breadth searches
        queue.append((-1, -1))
        # set the minutes
        minutes_elapsed = -1
        # loop until all the rotten oranges are depleted
        while queue:
            # get the index of rotten orange
            row, col = queue.popleft()
            # if the breadth search is completed
            if row == -1:
                # increase the number of minutes
                minutes_elapsed += 1
                # if there are more pending rotten oranges
                if queue:
                    # add the flag for next breadth search
                    queue.append((-1, -1))
            # if there is a rotten orange
            else:
                # contaminate its neighbors
                for d in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                    # if the row and col of the neighbor is within the grid
                    neighbor_row, neighbor_col = row + d[0], col + d[1]
                    if 0 <= neighbor_row < len(grid) and 0 <= neighbor_col < len(grid[0]):
                        # if the neighbor is fresh
                        if grid[neighbor_row][neighbor_col] == 1:
                            # contaminate the neighbor
                            grid[neighbor_row][neighbor_col] = 2
                            # decrease the number of fresh oranges
                            fresh_oranges -= 1
                            # add the new rotten orange to the queue
                            queue.append((neighbor_row, neighbor_col))
        # return elapsed minutes if no fresh orange left
        return minutes_elapsed if fresh_oranges == 0 else -1
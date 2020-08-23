class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # set the up the list of eight directions of the cell
        neighbors = [(1, 0), (0, 1), (1, 1), (-1, 0), (0, -1), (-1, -1), (-1, 1), (1, -1)]
        # set the number of rows
        rows = len(board)
        # set the number of columns
        cols = len(board[0])
        # iterate the board
        for row in range(rows):
            for col in range(cols):
                # set the temporary variable to count the neighbors
                live_neighbors = 0
                # scan all the neighbors of the cell
                for neighbor in neighbors:
                    r = row + neighbor[0]
                    c = col + neighbor[1]
                    # if the index does not exceed the board and the cells are alive
                    if (0 <= r < rows) and (0 <= c < cols) and abs(board[r][c]) == 1:
                        # increase the number of neighbor
                        live_neighbors += 1
                # if the current cell is alive and the neighbors are not 2 or 3
                if board[row][col] == 1 and not (live_neighbors == 2 or live_neighbors == 3):
                    # the current cell dies
                    board[row][col] = -1
                # if the current cell is dead and the total number of neighbors are 3
                if board[row][col] == 0 and live_neighbors == 3:
                    # the current cell lives
                    board[row][col] = 2

        # modfiy the -1 and 2 to get the correct return value
        for row in range(rows):
            for col in range(cols):
                if board[row][col] > 0:
                    board[row][col] = 1
                else:
                    board[row][col] = 0
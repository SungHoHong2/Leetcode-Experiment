class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        # set the up the list of eight directions of the cell
        directions = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]
        # set the length of row and column
        rows, cols = len(board), len(board[0])
        # copy the board used for checking the previous status
        copyBoard = [[board[r][c] for c in range(cols)] for r in range(rows)]
        # iterate the board
        for i in range(rows):
            for j in range(cols):
                # set the temporary variable to count the neighbors
                neighbors = 0
                # scan all the neighbors of the cell
                for r,c in directions:
                    # if the index does not exceed the board and the cells are alive
                    if 0<=(i+r)<rows and 0<=(j+c)<cols and copyBoard[i+r][j+c] == 1:
                        # increase the number of neighbor
                        neighbors += 1
                # if the current cell is alive and the neighbors are not 2 or 3
                if copyBoard[i][j] == 1 and not(neighbors==2 or neighbors==3):
                    # the current cell dies
                    board[i][j] = 0
                # if the current cell is dead and the total number of neighbors are 3
                if copyBoard[i][j] == 0 and neighbors == 3:
                    # the current cell lives
                    board[i][j] = 1
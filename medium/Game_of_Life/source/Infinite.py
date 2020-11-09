class Solution:
    def iteration(self, live):
        # set the hashmap to count the number of lives cells for the current cell
        counter = collections.defaultdict(int)
        # set the directions for the neighbor
        neighbors = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]
        # iterate the live cells
        for i, j in live:
            # get the neighbors of current live cell
            for ni, nj in neighbors:
                # increase the number of existing neighbors
                counter[(i+ni, j+nj)] += 1
        # set up a return hashset
        rtn = set()
        # iterate the counter hashmap
        for key, value in counter.items():
            # if the current cell is alive with 2 live neighbors or have 3 live neighbors
            if value == 3 or (value == 2 and key in live):
                # add the index to the return hashset
                rtn.add(key)
        # return the hashhset
        return rtn

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # set the variable of the row
        rows = len(board)
        # set the variable of the column
        cols = len(board[0])
        # set up the hashset to store the indexes of the live cell
        live = set()
        # iterate the board
        for row in range(rows):
            for col in range(cols):
                # if the cell is alive
                if board[row][col] == 1:
                    # add to the hashset
                    live.add((row, col))
        # return the alive cells after running the iteration function
        live = self.iteration(live)
        # iterate the board
        for row in range(rows):
            for col in range(cols):
                # update the live cells
                board[row][col] = int((row, col) in live)

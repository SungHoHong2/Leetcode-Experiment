class Solution:
    def iteration(self, live):
        # set the hashmap to count the number of lives cells for the current cell
        neighbors = collections.defaultdict(int)
        # set the directions for the neighbor
        directions = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]
        # iterate the live cells
        for i, j in live:
            # get the neighbors of current live cell
            for r, c in directions:
                # increase the number of existing neighbors
                neighbors[(i+r,c+j)] += 1
        # set up the hashset that collects the future live cells
        ans = set()
        # iterate the neighbors of the live cell
        for key, value in neighbors.items():
            # if the cell is alive with 2 live neighbors or have 3 live neighbors
            if value == 3 or (value == 2 and key in live):
                # add the index of the live cell
                ans.add(key)
        # return the future live cells
        return ans

    def gameOfLife(self, board: List[List[int]]) -> None:
        # set the length of the row and column
        rows, cols = len(board), len(board[0])
        # set up the hashset to store the indexes of the live cell
        live = set([(r,c) for c in range(cols) for r in range(rows) if board[r][c] == 1 ])
        # return the alive cells after running the iteration function
        nextLive = self.iteration(live)
        # allow one row of the board in memory when updating the live cell
        for i, row in enumerate(board):
            for j in range(len(row)):
                row[j] = int((i,j) in nextLive)

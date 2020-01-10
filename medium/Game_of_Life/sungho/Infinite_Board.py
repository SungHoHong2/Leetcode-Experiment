class Solution:

    def gameOfLifeInfinite(self, live):
        counter = {}
        # neighbors = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]

        # collect neighboring cells
        for i, j in live:
            for I in range(i - 1, i + 2):
                for J in range(j - 1, j + 2):
                    if I != i or J != j:
                        if (I, J) not in counter:
                            counter[(I, J)] = 1
                        else:
                            counter[(I, J)] += 1

        rtn = set()

        for c in counter:
            if counter[c] == 3 or counter[c] == 2 and c in live:
                rtn.add(c)

        return rtn

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows = len(board)
        cols = len(board[0])

        live = set()
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 1:
                    live.add((row, col))

        live = self.gameOfLifeInfinite(live)

        for row in range(rows):
            for col in range(cols):
                board[row][col] = int((row, col) in live)







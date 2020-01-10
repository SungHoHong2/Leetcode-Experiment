# 1. Any live cell with fewer than two live neighbors dies, as if caused by under-population.
# 2. Any live cell with two or three live neighbors lives on to the next generation.
# 3. Any live cell with more than three live neighbors dies, as if by over-population..
# 4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# perform simultaneous updation as is required in the question

class Solution:
    def gameOfLifeInfinite(self, live):
        ctr = collections.Counter((I, J)
                                  for i, j in live
                                  for I in range(i-1, i+2)
                                  for J in range(j-1, j+2)
                                  if I != i or J != j)
        return {ij
                for ij in ctr
                if ctr[ij] == 3 or ctr[ij] == 2 and ij in live}

    def gameOfLife(self, board):
        live = {(i, j) for i, row in enumerate(board) for j, live in enumerate(row) if live}
        live = self.gameOfLifeInfinite(live)
        for i, row in enumerate(board):
            for j in range(len(row)):
                row[j] = int((i, j) in live)
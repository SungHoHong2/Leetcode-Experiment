class Solution:
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        cnt = 0

        # construct 3x3 squares
        for i in range(1, len(grid) - 1):
            for j in range(1, len(grid[0]) - 1):
                temp = [[grid[i + x][j + y] for y in (-1, 0, 1)] for x in (-1, 0, 1)]

                if self.isMagicSquare(temp):
                    cnt += 1

                    # return the number of magic squares
        return cnt

    def isMagicSquare(self, grid):
        '''
        Check whether the given grid is a magic square
        '''
        # Check the elements
        flat = [num for row in grid for num in row]

        # if all the elements in the square does not contain numbers from 1 to 9
        if sorted(flat) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            return False

        # the sum of the row, col and diaganal
        row_sums = [sum(row) for row in grid]
        col_sums = [sum([row[i] for row in grid]) for i in range(3)]
        diag_sums = [(grid[0][0] + grid[1][1] + grid[2][2]), (grid[0][2] + grid[1][1] + grid[2][0])]

        # merge all the results into one list
        row_sums.extend(col_sums)
        row_sums.extend(diag_sums)

        # check whether all the sums have the same value (15)
        return len(set(row_sums)) == 1
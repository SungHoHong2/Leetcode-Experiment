class Solution(object):
    def spiralOrder(self, matrix):
        # if the matrix is empty
        if not matrix:
            # return a empty row
            return []
        # get the number of rows and cols
        R, C = len(matrix), len(matrix[0])
        # create the matrix for checking the visited cells
        seen = [[False for i in range(C)] for j in range(R)]
        # initialize a list for return
        ans = []
        # set the order of direction for the row (down,up)
        dr = [0, 1, 0, -1]
        # set the order of direction for the column (right,left)
        dc = [1, 0, -1, 0]
        # initalize the pointers for the direction
        r = c = di = 0
        # iterate the total number of cells in the matrix
        for _ in range(R * C):
            # append the current cell
            ans.append(matrix[r][c])
            # set the current cell visited
            seen[r][c] = True
            # move the current cell using the current direction (right,down,left,up)
            cr, cc = r + dr[di], c + dc[di]
            # if the cell is within the matrix and it is not visited
            if 0 <= cr < R and 0 <= cc < C and not seen[cr][cc]:
                # follow the current direction
                r, c = cr, cc
            # if the cell exceeds the matrix
            else:
                # change the direction
                di = (di + 1) % 4
                # update the current cell
                r, c = r + dr[di], c + dc[di]
        # return the answer
        return ans
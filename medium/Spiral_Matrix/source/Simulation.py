class Solution(object):
    def spiralOrder(self, matrix):
        # if the matrix is empty
        if not matrix:
            # return a empty row
            return list()
        # get the number of rows and cols
        rows, cols = len(matrix), len(matrix[0])
        # create the matrix for checking the visited cells
        visited = [[0 for c in range(cols)] for r in range(rows)]
        # initialize a list for return
        ans = list()
        # set the order of direction (right,down,left,up)
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        # initialize the index for the matrix and the direction
        r,c,d = 0,0,0
        # iterate the total number of cells in the matrix
        for _ in range(rows * cols):
            # append the current cell
            ans.append(matrix[r][c])
            # set the current cell visited
            visited[r][c] = 1
            # move the current cell using the current direction (right,down,left,up)
            i, j = r + directions[d][0], c + directions[d][1]
            # if the cell is within the matrix and it is not visited
            if 0<=i<rows and 0<=j<cols and not visited[i][j]:
                # follow the current direction
                r, c = i, j
            # if the cell exceeds the matrix
            else:
                # change the direction
                d = (d + 1) % 4
                # update the current cell
                r, c = r + directions[d][0], c + directions[d][1]
        # return the answer
        return ans
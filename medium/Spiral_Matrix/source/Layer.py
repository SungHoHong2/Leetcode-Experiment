class Solution(object):
    def spiralOrder(self, matrix):
        # set the list for return
        ans = list()
        # return empty array if the matrix is empty
        if not matrix:
            return ans
        # set the length of the row and the column
        rows, cols = len(matrix), len(matrix[0])
        # set the pointer for iteration and the maximum number of iteration
        iterations = min(rows,cols)
        # set the start point of the row and column
        r,c = 0,0
        # two iterations cover one layer of the matrix
        for iteration in range(iterations):
            # even number of iteration
            if iteration % 2 == 0:
                # collect the top side of the layer
                for i in range(c, cols):
                    ans.append(matrix[r][i])
                # collect the right side of the layer
                for i in range(r+1, rows):
                    ans.append(matrix[i][cols-1])
                # shrink the layer for the odd iteration
                r,cols = r+1, cols-1
            # odd number of iteration
            else:
                # collect the bottom side of the layer
                for i in reversed(range(c, cols)):
                    ans.append(matrix[rows-1][i])
                # collect the left side of the layer
                for i in reversed(range(r, rows-1)):
                    ans.append(matrix[i][c])
                # shrink the layer for the even iteration
                c, rows = c+1, rows-1
        # return the list
        return ans
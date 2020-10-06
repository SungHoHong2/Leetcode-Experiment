class Solution(object):
    def spiralOrder(self, matrix):

        # set the list for return
        ans = []
        # if the matrix is empty
        if not matrix:
            # return empty array
            return ans
        # set the length of the row and the column
        R, C = len(matrix), len(matrix[0])
        # set the pointer for iteration and the maximum number of interation
        iteration, max_iteration = 0, min(R, C)
        # set the start point of the row and column
        r = c = 0
        # iterate the total number of matrix
        # two iterations cover one layer of the matrix
        while iteration < max_iteration:
            # even number of iteration
            if iteration % 2 == 0:
                # collect the top side of the layer
                for j in range(c, C):
                    ans.append(matrix[r][j])
                # collect the right side of the layer
                for i in range(r + 1, R):
                    ans.append(matrix[i][C - 1])
                # shrink the layer
                r, C = r + 1, C - 1
            # odd number of iteration
            else:
                # collect the bottom side of the layer
                for i in reversed(range(c, C)):
                    ans.append(matrix[R - 1][i])
                # collect the left side of the layer
                for i in reversed(range(r, R - 1)):
                    ans.append(matrix[i][c])
                # shrink the layer
                c, R = c + 1, R - 1
            # increase iteration
            iteration += 1
        # return the list
        return ans
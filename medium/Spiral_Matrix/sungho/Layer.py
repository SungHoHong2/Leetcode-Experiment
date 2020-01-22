class Solution(object):
    def spiralOrder(self, matrix):

        if not matrix: return []
        # return the answer
        ans = []

        # get the index of the first row and the last row
        r1, r2 = 0, len(matrix) - 1

        # get the index of the first column and the last column
        c1, c2 = 0, len(matrix[0]) - 1

        # iterate through the matrix
        while r1 <= r2 and c1 <= c2:

            # if the sprial coords return the result
            for c in range(c1, c2 + 1):
                ans.append(matrix[r1][c])

            # return all the elements from the right
            for r in range(r1 + 1, r2 + 1):
                ans.append(matrix[r][c2])

            if r1 < r2 and c1 < c2:

                # return all the elements from the bottom
                for c in range(c2 - 1, c1, -1):
                    ans.append(matrix[r2][c])

                # return all the elements from the left
                for r in range(r2, r1, -1):
                    ans.append(matrix[r][c1])

            # reduce the layers
            r1 += 1;
            r2 -= 1
            c1 += 1;
            c2 -= 1
        return ans
class Solution:
    def search_rec(self,left, up, right, down):
        # return false if the submatrix is empty
        if left > right or up > down:
            return False
        # return false if the `target` is not in top-left and bottom-right submatrice
        elif self.target < self.matrix[up][left] or self.target > self.matrix[down][right]:
            return False
        # get the pivot
        mid = left + (right-left) // 2
        # locate `row` such that matrix[row-1][mid] < target < matrix[row][mid]
        row = up
        while row <= down and self.matrix[row][mid] <= self.target:
            # return true if the target is found while locating the middle
            if self.matrix[row][mid] == self.target:
                print((left, up, right, down), mid, row)
                return True
            row += 1
        # invoke recursions for the bottom-left and the top-right submatrice
        return self.search_rec(left, row, mid-1, down) or self.search_rec(mid+1, up, right, row-1)

    def searchMatrix(self, matrix, target):
        # set the target variable to global
        self.target = target
        # set the matrix variable to global
        self.matrix = matrix
        # if the input is empty
        if not matrix:
            # return false
            return False
        # invoke recursion
        return self.search_rec(0, 0, len(matrix[0])-1, len(matrix)-1,)
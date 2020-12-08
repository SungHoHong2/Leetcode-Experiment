class Solution:
    def search_rec(self,left, up, right, down):
        # return false if the target does not exist
        if left > right or up > down:
            return False
        # return false if the `target` is within the in top-left and bottom-right submatrices
        elif self.target < self.matrix[up][left] or self.target > self.matrix[down][right]:
            return False
        # get the horizontal pivot
        mid = left + (right-left) // 2
        # get the veritcal pivot
        row = up
        while row <= down and self.matrix[row][mid] <= self.target:
            # return true if the target is found while locating the middle
            if self.matrix[row][mid] == self.target:
                return True
            row += 1
        # explore the target in the bottom-left and the top-right submatrices
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
        return self.search_rec(0, 0, len(matrix[0])-1, len(matrix)-1)
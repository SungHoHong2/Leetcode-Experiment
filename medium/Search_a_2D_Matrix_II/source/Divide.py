class Solution:
    def recursion(self, target, left, up, right, down):
        """
        target = 5
        [ 1,2,  3, [4,5]]
        [ 2,3, [4],[5,6]]
        [[3,4],[6], 8,9]
        [[4,5], 7,  8,9]
        once the target is between the two rows, the target is in down,left or top,right
        """
        # return false if the target does not exist
        if left > right or up > down:
            return False
        # return false if the target is within the in top-left and bottom-right submatrices
        elif self.matrix[up][left] > target or self.matrix[down][right] < target:
            return False
        # get the horizontal pivot
        mid_col = left + (right - left) // 2
        # get the vertical pivot == matrix[row-1][mid] < target < matrix[row][mid]
        mid_row = up
        while mid_row <= down and self.matrix[mid_row][mid_col] <= target :
            # return true if the target is found while locating the middle
            if target == self.matrix[mid_row][mid_col]:
                return True
            mid_row += 1
        # explore the target in the bottom-left and the top-right submatrices
        return self.recursion(target, left, mid_row, mid_col-1, down) or self.recursion(target, mid_col+1, up, right, mid_row-1)

    def searchMatrix(self, matrix, target):
        # set the matrix variable to global
        self.matrix = matrix
        # return false if the input is empty
        if not matrix:
            return False
        # invoke recursion
        return self.recursion(target, 0, 0, len(matrix[0])-1, len(matrix)-1)
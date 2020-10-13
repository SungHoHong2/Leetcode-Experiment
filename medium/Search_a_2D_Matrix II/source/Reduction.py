class Solution:
    def searchMatrix(self, matrix, target):
        # return false if there is no input
        if not matrix:
            return False
        # start our "pointer" from the bottom-left
        row = len(matrix)-1
        col = 0
        # loop until the pointer reaches the top-right
        while col < len(matrix[0]) and row >= 0:
            # move up if the target is smaller than the current value
            if matrix[row][col] > target:
                row -= 1
            # move right if the target is larger than the current value
            elif matrix[row][col] < target:
                col += 1
            # return true if found
            else:
                return True
        # return false if not found
        return False
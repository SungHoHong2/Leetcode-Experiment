class Solution:
    def binary_search(self, target, start, vertical):
        # set the lowest index
        low = start
        # set the highest index for vertical or horizontal
        high = len(self.matrix)-1 if vertical else len(self.matrix[0])-1
        # loop until the lowest index meets the highest
        while low <= high:
            # get the middle
            mid = (low + high) // 2
            # if it is a vertical search
            if vertical:
                # binary search the rows
                if self.matrix[mid][start] < target:
                    low = mid + 1
                elif self.matrix[mid][start] > target:
                    high = mid -1
                else:
                    return True
            # if it is a horizontal search
            else:
                # binary search the columns
                if self.matrix[start][mid] < target:
                    low = mid + 1
                elif self.matrix[start][mid] > target:
                    high = mid -1
                else:
                    return True
        # return false if no target was found
        return False

    def searchMatrix(self, matrix, target):
        # return false if the matrix is empty
        if not matrix:
            return False
        # globalize the input
        self.matrix = matrix
        # iterate the matrix diagonally
        for i in range(min(len(matrix), len(matrix[0]))):
            # binary search the target vertically
            vertical = self.binary_search(target, i, True)
            # binary search the target horizontally
            horizontal = self.binary_search(target, i, False)
            # return true if the target is found
            if vertical or horizontal:
                return True
        # return false if the target was not found with binary search
        return False
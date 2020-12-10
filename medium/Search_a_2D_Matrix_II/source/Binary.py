class Solution:
    def binary_search(self, matrix, target, start, vertical):
        # set the lowest index
        lo = start
        # set the highest index for vertical or horizontal
        hi = len(matrix)-1 if vertical else len(matrix[0])-1
        # loop until the lowest index meets the highest
        while hi >= lo:
            # get the middle
            mid = (lo + hi) // 2
            # if it is a horizontal search
            if not vertical:
                # binary search the columns
                if matrix[start][mid] < target:
                    lo = mid + 1
                elif matrix[start][mid] > target:
                    hi = mid - 1
                else:
                    return True
            # if it is a vertical search
            else:
                # binary search the rows
                if matrix[mid][start] < target:
                    lo = mid + 1
                elif matrix[mid][start] > target:
                    hi = mid - 1
                else:
                    return True
        # return false if no target was found
        return False

    def searchMatrix(self, matrix, target):
        # if there is not input
        if not matrix:
            # return false
            return False

        # iterate the matrix diagonally
        for i in range(min(len(matrix), len(matrix[0]))):
            # binary search the target vertically
            vertical_found = self.binary_search(matrix, target, i, True)
            # binary search the target horizontally
            horizontal_found = self.binary_search(matrix, target, i, False)
            # if the target is found
            if vertical_found or horizontal_found:
                # return true
                return True
        # return false if the target was not found with binary search
        return False
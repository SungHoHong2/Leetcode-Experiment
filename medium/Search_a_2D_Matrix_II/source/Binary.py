class Solution:
    def binarySearch(self, matrix, target, start, vertical):
        # set the lowest index
        low = start
        # set the highest index for vertical or horizontal
        high = len(matrix)-1 if vertical else len(matrix[0])-1
        # loop until the lowest index meets the highest
        while low <= high:
            # get the middle
            mid = (low + high) // 2
            # if it is a vertical search
            if vertical:
                # binary search the rows
                if matrix[mid][start] < target:
                    low = mid + 1
                elif matrix[mid][start] > target:
                    high = mid -1
                else:
                    return True
            # if it is a horizontal search
            else:
                # binary search the columns
                if matrix[start][mid] < target:
                    low = mid + 1
                elif matrix[start][mid] > target:
                    high = mid -1
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
            vertical = self.binarySearch(matrix,target,i,True)
            # binary search the target horizontally
            horizontal = self.binarySearch(matrix,target,i,False)
            # if the target is found
            if vertical or horizontal:
                # return true
                return True
        # return false if the target was not found with binary search
        return False
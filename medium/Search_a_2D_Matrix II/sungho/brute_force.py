class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        for rows in matrix:
            for item in rows:
                if item == target:
                    return True

        return False



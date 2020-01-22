class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        m = len(matrix)
        n = len(matrix[0])
        up = 0
        down = m - 1
        left = 0
        right = n - 1
        result = []
        while len(result) < m * n:
            for j in range(left, right + 1):
                if len(result) < m * n:
                    result.append(matrix[up][j])
            for i in range(up + 1, down):
                if len(result) < m * n:
                    result.append(matrix[i][right])
            for j in range(right, left - 1, -1):
                if len(result) < m * n:
                    result.append(matrix[down][j])
            for i in range(down - 1, up, -1):
                if len(result) < m * n:
                    result.append(matrix[i][left])
            print result
            left += 1
            right -= 1
            up += 1
            down -= 1

        return result

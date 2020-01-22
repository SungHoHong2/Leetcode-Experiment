class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        result = []
        m = len(matrix)
        n = len(matrix[0])
        seen = [[False] * n for j in range(m)]
        rdir = [0, 1, 0, -1]
        cdir = [1, 0, -1, 0]
        i = j = 0
        di = 0
        for x in range(m * n):

            result.append(matrix[i][j])
            seen[i][j] = True
            ni = i + rdir[di]
            nj = j + cdir[di]
            if 0 <= ni < m and 0 <= nj < n and not seen[ni][nj]:

                i = ni
                j = nj
            else:
                di = (di + 1) % 4

                i = i + rdir[di]
                j = j + cdir[di]
                print i, j

        return result
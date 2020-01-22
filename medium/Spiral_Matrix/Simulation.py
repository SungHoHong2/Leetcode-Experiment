class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []

        # total size of the row and the colums
        R, C = len(matrix), len(matrix[0])

        # create the matrix table that has the status unseen
        seen = [[False] * C for _ in matrix]

        # the answers that will be returned
        ans = []

        # explanation of the direction
        # 1. right
        # 2. down
        # 3. left
        # 4. up

        # directions of the row
        dr = [0, 1, 0, -1]

        # directions of the columns
        dc = [1, 0, -1, 0]

        # index for row, col, and direction
        r = c = di = 0

        # iterate through all of the matrix
        for _ in range(R * C):

            # add the column to the answer and mark it as true
            ans.append(matrix[r][c])
            seen[r][c] = True

            # follow the direction
            cr, cc = r + dr[di], c + dc[di]

            # if the column and the row is within the matrix and it is unseen
            if 0 <= cr < R and 0 <= cc < C and not seen[cr][cc]:
                # move on
                r, c = cr, cc

            # if the direction index reached the limit
            else:
                # update the direction index
                di = (di + 1) % 4
                # change the direction
                r, c = r + dr[di], c + dc[di]

        return ans
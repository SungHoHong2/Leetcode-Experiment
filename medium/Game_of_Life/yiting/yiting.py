class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        new = [[board[i][j] for j in range(len(board[0]))] for i in range(len(board))]

        for i in range(len(board)):
            for j in range(len(board[0])):

                live = 0

                for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1), (i - 1, j - 1), (i + 1, j + 1),
                             (i + 1, j - 1), (i - 1, j + 1)]:
                    if x >= 0 and x < len(board) and y >= 0 and y < len(board[0]):

                        # print x,y
                        if new[x][y] == 1:
                            live += 1

                if new[i][j] == 0 and live == 3:
                    board[i][j] = 1
                elif new[i][j] == 1 and live < 2:
                    board[i][j] = 0
                elif new[i][j] == 1 and live == 2 or live == 3:
                    board[i][j] = 1
                elif new[i][j] == 1 and live > 3:
                    board[i][j] = 0





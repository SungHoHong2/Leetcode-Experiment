class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        # store the basic information of the table
        self.ROWS = len(board)
        self.COLS = len(board[0])
        self.board = board

        # traverse through all the possible cells
        for row in range(self.ROWS):
            for col in range(self.COLS):
                if self.backtrack(row, col, word):
                    return True

        # if found the snake in the table return True else False
        return False

        # checks the first element of the word and keep exploring by removing the first element

    def backtrack(self, row, col, suffix):

        # if there all the word is searched return True
        if len(suffix) == 0:
            return True

        # validity check:
        #   if row or column exceeds the border or the target cell does not match with the first element of the word
        #   return false
        if row < 0 or row == self.ROWS or col < 0 or col == self.COLS or self.board[row][col] != suffix[0]:
            return False

            # mark the word as searched
        self.board[row][col] = '#'

        # traverse the neighboring elements
        for rowOffset, colOffset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            # if the word is found break
            if self.backtrack(row + rowOffset, col + colOffset, suffix[1:]):
                return True

        # return back to original state
        self.board[row][col] = suffix[0]

        # return
        return False
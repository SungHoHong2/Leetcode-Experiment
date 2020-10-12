class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # set the table as the global pointer
        self.board = board
        # iterate all possible cells
        for row in range(len(board)):
            for col in range(len(board[0])):
                # invoke recursion
                if self.backtrack(row, col, word):
                    # return true if the snake is found
                    return True
        # return false if the snake is not found
        return False

    def backtrack(self, row, col, suffix):
        # if the snake is completed
        if len(suffix) == 0:
            # return true
            return True
        # if the row and column exceeds the table or the target character does no create the snake
        if not(0<=row<len(self.board)) or not(0<=col<len(self.board[0])) or self.board[row][col] != suffix[0]:
            return False
        # mark the word as searched to prevent infinite loop
        self.board[row][col] = '#'
        # traverse the neighboring elements
        for rowOffset, colOffset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            # if the snake is found from the recursion
            if self.backtrack(row + rowOffset, col + colOffset, suffix[1:]):
                # return true
                return True
        # return back to original state to allow other recursions to search for the snake
        self.board[row][col] = suffix[0]
        # return false is no snake is found
        return False
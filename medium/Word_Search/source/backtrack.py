class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # set the table as the global pointer
        self.board = board
        # iterate all possible cells in the board
        for i in range(len(board)):
            for j in range(len(board[0])):
                # return true if the snake is found from the recursion
                if self.backtrack(i,j,word):
                    return True
        # return false if the snake is not found
        return False

    def backtrack(self, row, col, suffix):
        # return true if the snake is completed
        if not suffix:
            return True
        # return false if the index exceeds the board or the suffix does not match
        if not(0<=row<len(self.board)) or not(0<=col<len(self.board[0])) or suffix[0] != self.board[row][col]:
            return False
        # mark the index as visited
        self.board[row][col] = '#'
        # traverse the neighboring elements
        for r,c in [(1,0),(0,1),(-1,0),(0,-1)]:
            # return true if the snake is found from the recursion
            if self.backtrack(row+r, col+c, suffix[1:]):
                return True
        # reset the table back to original state to allow other recursions to search
        self.board[row][col] = suffix[0]
        # return false when no snake is found
        return False
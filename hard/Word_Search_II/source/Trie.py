class Solution:
    def backtracking(self, row, col, parent):
        # get the letter from the current cell
        letter = self.board[row][col]
        # get the current node of the Trie
        currNode = parent[letter]

        # check if we find a match of word
        if '$' in currNode:
            self.matchedWords.append(currNode['$'])
            del currNode['$']

        # mark the cell as visited
        self.board[row][col] = '#'

        # explore the neighbors
        for directions in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            newRow, newCol = row + directions[0], col + directions[1]
            # continue if the row or column exceeds the board
            if not (0 <= newRow < len(self.board)) or not (0 <= newCol < len(self.board[0])):
                continue
            # continue if the letter does not match the Trie
            if not self.board[newRow][newCol] in currNode:
                continue
            # explore deeper
            self.backtracking(newRow, newCol, currNode)

        # restore the cell
        self.board[row][col] = letter

        # incrementally remove the matched leaf node in Trie to prune the nodes in Trie
        if not currNode:
            del parent[letter]

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.board, self.words = board, words
        # set a Trie using the input
        trie = {}
        for word in words:
            node = trie
            # store the word in the Trie
            for letter in word:
                if letter not in node:
                    node[letter] = dict()
                node = node[letter]
            # mark the existence of a word in trie node
            node['$'] = word
        # set a variable to collect the matched words
        self.matchedWords = []
        # iterate the row of the board
        for row in range(len(board)):
            # iterate the column of the board
            for col in range(len(board[0])):
                # if the letter matches with the starting letter of the Trie
                if board[row][col] in trie:
                    # invoke the backtracking
                    self.backtracking(row, col, trie)
        # return the collected matched words
        return self.matchedWords
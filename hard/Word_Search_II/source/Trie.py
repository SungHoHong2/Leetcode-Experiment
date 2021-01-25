class Solution:
    def backtracking(self, row, col, parent):
        # set an return array
        res = list()
        # get the letter from the current cell
        letter = self.board[row][col]
        # get the current node of the Trie
        currNode = parent[letter]
        # if the matching word is found
        if '$' in currNode:
            # append the word to the returning array
            res.append(currNode['$'])
            # remove the sentinel to find the word only once
            del currNode['$']
        # mark the cell as visited
        self.board[row][col] = '#'
        # explore the neighbors
        for r,c in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            i, j = row + r, col + c
            # continue if the row or column exceeds the board
            if not (0 <= i < len(self.board)) or not (0 <= j < len(self.board[0])):
                continue
            # continue if the letter does not match the Trie
            if not self.board[i][j] in currNode:
                continue
            # explore deeper
            res += self.backtracking(i, j, currNode)
        # restore the cell
        self.board[row][col] = letter
        # incrementally remove the chars of the matched word for pruning
        if not currNode:
            del parent[letter]
        return res

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # globalize the input
        self.board, self.words = board, words
        # create a Trie
        trie = {}
        # iterate the words
        for word in words:
            # set the current layer of the trie
            node = trie
            # iterate the chars in the word
            for char in word:
                # create a new layer if the char does not exist
                if char not in node:
                    node[char] = dict()
                # move on to the next layer
                node = node[char]
            # add a sentinel layer once the word is reached
            node['$'] = word
        # set a returning array that collects the matched words
        res = list()
        # iterate the row of the board
        for row in range(len(board)):
            # iterate the column of the board
            for col in range(len(board[0])):
                # if the character matches with the first layer of the Trie
                if board[row][col] in trie:
                    # collect the matched words from  backtracking
                    res += self.backtracking(row, col, trie)
        # return the collected matched words
        return res
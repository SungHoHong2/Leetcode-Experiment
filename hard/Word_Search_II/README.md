### Word Search II
**Backtracking with Trie**
- [Source code](source/Trie.py)

```python
class Solution:
    def backtracking(self, row, col, parent):
        # set an return array 
        # get the letter from the current cell
        # get the current node of the Trie
        # if the matching word is found 
            # append the word to the returning array 
            # remove the sentinel to find the word only once 
        # mark the cell as visited
        # explore the neighbors
            # continue if the row or column exceeds the board
            # continue if the letter does not match the Trie
            # explore deeper
        # restore the cell
        # incrementally remove the chars of the matched word for pruning 
        pass

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # globalize the input 
        # create a Trie
        # iterate the words 
            # set the current layer of the trie
            # iterate the chars in the word 
                # create a new layer if the char does not exist 
                # move on to the next layer
            # add a sentinel layer once the word is reached  
        # set a returning array that collects the matched words
        # iterate the row of the board
            # iterate the column of the board
                # if the character matches with the first layer of the Trie
                    # collect the matched words from  backtracking
        # return the collected matched words
        pass
```

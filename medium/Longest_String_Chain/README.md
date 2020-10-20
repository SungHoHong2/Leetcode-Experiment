### Longest String Chain
**Dynamic Programming**
- [Source code](source/dp.py)
```python
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # set the map for tracking the results of the subproblems
        # set the variable to return the number of possible chains
        # sort the words by length
        # iterate the words
            # store the current word as a key
            # iterate each indexes of the word 
                # generate a word that excludes the ith index
                # if the generated word exists in the map
                    # update the possible chain of the current word
                    # keep track of the maximum length of the chain
        # return the maximum length of the chain
        pass
```

### Verifying an Alien Dictionary
**Check Adjacent Words**
- [source code](source/adjacent.py)
```python
class Solution(object):
    def isAlienSorted(self, words, order):
        # set the hashmap that records the key as the char and the value as the order 
        # iterate the words 
            # get the first word 
            # get the second word 
            # set a flag for identical words 
            # iterate the shortest word 
                # if the characters are not identical 
                    # if the order of the characters are wrong
                        # return false
                    # if the order is correct 
                        # the word is not identical and don't need to compare anymore  
            # if the word is identical but the length of the first word is longe
                # return false 
        # return true if there is no problems
```
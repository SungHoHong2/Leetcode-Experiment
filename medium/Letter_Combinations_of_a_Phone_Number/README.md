### Letter Combinations of a Phone Number
**Backtracking**
- [Source code](source/Backtrack.py)
```python
class Solution:
    def backtrack(self, combination, next_digits):
        # if recursive tree has reached its leaf
            # append the finished combination to the return list
        # if there are still digits to check
            # iterate the letters which are mapped to the number
                # provide the combination and the next digit to the next recursive tree
        pass 

    def letterCombinations(self, digits):
        # set the map for all the characters mapped to the number
        self.phone = {'2': ['a', 'b', 'c'],
                      '3': ['d', 'e', 'f'],
                      '4': ['g', 'h', 'i'],
                      '5': ['j', 'k', 'l'],
                      '6': ['m', 'n', 'o'],
                      '7': ['p', 'q', 'r', 's'],
                      '8': ['t', 'u', 'v'],
                      '9': ['w', 'x', 'y', 'z']}
        # set the return list
        # if there is no input
            # return the empty list
            # invoke the recursive function
        # return the list 
        pass 
```

### Letter Combinations of a Phone Number
**Backtracking**
- Concepts 
    - Use a global hashmap that stores the list of characters for each numbers
    - Use recursion to print out all the possible combinations
- [Source code](source/Backtrack.py)
```python
class Solution:
    def backtrack(self, combination, next_digits):
        # append the combination to the return list if the input is depleted
        # if there are still digits to check
            # iterate the letters which are mapped to the number
                # provide the combination and the next digit to the next recursive tree
        pass

    def letterCombinations(self, digits):
        # set the map for all the characters mapped to the number
        # set the answer as an array
        # return the answer if there is no input
        # invoke the recursive function
        # return the list
        pass
```

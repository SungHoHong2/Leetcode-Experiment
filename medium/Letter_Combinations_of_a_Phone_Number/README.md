### Letter Combinations of a Phone Number
**Backtracking**
- Concepts 
    - Use a global hashmap that stores the list of characters for each numbers
    - Use recursion to print out all the possible combinations
- [Source code](source/Backtrack.py)
```python
class Solution:
    def recursion(self, combination, next_digits):
        # set a return array that stores all the combinations 
        # return the combination to the return list if the input is depleted
        # iterate the letters which are mapped to the number
            # extend the combinations to the return array 
        # return the combinations
        pass

    def letterCombinations(self, digits: str) -> List[str]:
        # return an empty list if there is no input 
        # create a dictionary that maps all the letters with the numbers
        self.phone = {'2': ['a', 'b', 'c'],
                      '3': ['d', 'e', 'f'],
                      '4': ['g', 'h', 'i'],
                      '5': ['j', 'k', 'l'],
                      '6': ['m', 'n', 'o'],
                      '7': ['p', 'q', 'r', 's'],
                      '8': ['t', 'u', 'v'],
                      '9': ['w', 'x', 'y', 'z']}        
        # return the combination from the recursion 
        pass
```

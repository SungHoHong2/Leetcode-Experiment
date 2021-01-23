### Generate Parentheses
**Brute Force**
- [Concepts](images/Brute.png)
    - Computes every possible solution to a problem 
    - Selects one that fulfills the requirements
- [Recursion v2](source/Recursion2.py)

```python
class Solution(object):
    def generate(self, ans):
        # set up the return array
        # if the generated answer has the expected length
            # if the generated array contains
                # add the answer to the return list
        # if the generated answer does not have the expected length
            # invoke the recursive with additional opening
            # invoke the recursive with additional closing 
        # return the parentheses
        pass
        
    def valid(self, ans):
        # set the balance to check the validity of the parenthesis
        # iterate the list
            # if the list contains opening increment the balance
            # if the list contains closing decrement the balance
            # if the number of closing is more than the opening
        # return true if the number of opening and closing are equal
        pass
        
    def generateParenthesis(self, n):
        # set the total size of the parenthesis
        # return the list of answers from the recursion 
        pass
```

**Backtracking**
- [Concepts](images/Backtrack.png)
    - Extension of the Brute Force 
    - Potential solutions can be discarded before they have been finished
- [Backtrack v3](source/BackTracking3.py)

```python
class Solution(object):
    def backtrack(self, ans, left, right):
        # set up the return array
        # if the answer has the expected length
            # include the answer to the return array
        # if the length of the generated string is not enough
            # if the number of opening is not enough
                # run the recursion with additional opening
            # if the number of closing is smaller than opening
                # run the recursion with additional closing
        # return the parentheses
        pass
        
    def generateParenthesis(self, n):
        # set the total size of the valid parenthesis
        # run the recursion function
        pass
```
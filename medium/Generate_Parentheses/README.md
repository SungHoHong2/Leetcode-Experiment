### Generate Parentheses
**Brute Force**
- [Concepts](images/Brute.png)
    - Computes every possible solution to a problem 
    - Selects one that fulfills the requirements
- [Recursion v2](source/Recursion2.py)
- [Recursion v1](source/Recursion.py)

```python
class Solution(object):
    def generate(self, ans):
        # if the generated answer has the expected length
            # if the generated array contains
                # add the answer to the return list
        # if the generated answer does not have the expected length
            # invoke the recursive with additional opening
            # invoke the recursive with additional closing 
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
        # set up the return array
        # set the total size of the parenthesis
        # invoke the generate function
        # return the list of answers
        pass
```

**Backtracking**
- [Concepts](images/Backtrack.png)
    - Extension of the Brute Force 
    - Potential solutions can be discarded before they have been finished
- [Backtrack v3](source/BackTracking3.py)
- [Backtrack v2](source/BackTracking2.py)
- [Backtrack v1](source/BackTracking.py)

```python
class Solution(object):
    def backtrack(self, ans, left, right, ansSize, rtnArray):
        # if the answer has the expected length
            # include the answer to the return array
            # finish the recursive function
        # if the number of opnening is not enough
            # create an answer with additional opening
        # if the number of closing is smaller than opening
            # create an answer with additional closing
        pass
    def generateParenthesis(self, N):
        # set the return list
        # run the backtrack function
        # return the list of answers
        pass
```
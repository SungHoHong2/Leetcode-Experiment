### Generate Parentheses
**Brute Force**
- [Concepts](images/Brute.png)
    - computes every possible solution to a problem 
    - selects one that fulfills the requirements
- [Source code](source/Recursion.py)
```python
class Solution(object):
    def generate(self, ans, ansSize, rtnArray):
        # if the generated answer has the expected length
            # if the generated array contains
                # add the answer to the return list
        # if the generated answer does not have the expected length
            # append opening
            # go to the right child of the recursive tree
            # go back to the parent
            # append closing
            # go to the left child of the recursive tree
            # go back to the parent of the recursive tree
        pass
    def valid(self, A):
        # initiate a flag for checking the balance
        # iterate the list
            # if the list contains opening increment the balance
            # if the list contains closing decrement the balance
            # if the number closing is more than the opening
        # return true if the number of opening and closing are equal
        pass
    def generateParenthesis(self, n):
        # set up the return array
        # invoke the generate function
        # return the list of answers
        pass
```

**Backtracking**
- [Concepts](images/Backtrack.png)
    - Extension of the Brute Force 
    - Potential solutions can be discarded before they have been finished
- [Source code](source/BackTracking.py)
- [Source code2](source/BackTracking2.py)

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

**Closure Number**
- [Concepts](images/Closure.png)
- [Source code](source/Closure.py)
- [Source code (Applied Memoization)](source/Closure_DP.py)
```python
class Solution(object):
    def generateParenthesis(self, N):
        # return empty list when the answer expects zero Parentheses
        # set the returning list
        # iterate the available total number of parenthesis
            # get the list of answers when the number of opening is "c"
                # get the list of answers when the number of opening is N - c - 1
                    # generate the answer and add to the returning list
        # return the list of answers
        pass
```
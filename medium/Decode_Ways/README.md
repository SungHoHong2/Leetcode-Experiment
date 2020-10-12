### Decode Ways
**Recursive Approach with Memoization**
- [Concepts](images/memoization.png)
- [Source code](source/memoization.py)
```python
class Solution:
    def __init__(self):
        # set a map to record the possible characters
        pass

    def recursive_with_memo(self, index, s) -> int:
        # if the recursive tree reaches the largest index
        # If the string starts with a zero, it can't be decoded
        # if the recursive tree reaches the second largest index
        # return the recorded result if the same number is found
        # get the results from the recursive function using a single number and valid two digit number
        # record the result for the current number
        # return the result
        pass

    def numDecodings(self, s: str) -> int:
        # if there is no input
            # return 0
        # invoke the recursive tree
        pass
```

**Iterative Approach**
- [Concepts](images/iteration.png)
- [Source code](source/iteration.py)
```python
class Solution(object):
    def numDecodings(self, s):
        # if there is no input
            # return zero
        # set the list to store the subproblem results
        # initialize the list
        # update the first number to 1 unless it is a zero
        # record all the subproblem results
            # if the number is not a zero
                # accumulate the number to the dp list
            # get the two digit number
            # if the two digit number is a valid number
                # accumulate the number to the dp list
        # return the final result of the dp list
        pass
```

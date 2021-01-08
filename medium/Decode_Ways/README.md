### Decode Ways
**Recursive Approach with Memoization**
- [Concepts](images/memoization.png)
- [Concepts2](images/memoization2.png)
    - `dp[i]` is the number of ways of decoding substring `s[:i]`
    - `dp[i] = dp[i-1] + dp[i-2]`
        - Accumulate the possible results of both two digits and one digit
    - `dp[i] = dp[i-1] + 0`
        - Accumulate the possible result of one digit 

- [Source code](source/memoization.py)
```python
class Solution:
    def __init__(self):
        # set a map to record the possible characters
        pass

    def recursive(self, index, s) -> int:
        # return 1 if the last two digits are valid
        # return 0 if the last single digit is zero (invalid)
        # return 1 if the last single digit is valid
        # return the cached result if the rightside of the digits are visited
        # get the combinations from a single digit
        # get the combinations from a double digit if it is valid
        # record the possible combinations for the current digit
        # return the result
        pass

    def numDecodings(self, s: str) -> int:
        # return 0 if there is no input
        # invoke the recursion
        pass
```

**Iterative Approach**
- [Concepts](images/iteration.png)
- [Source code](source/iteration.py)
```python
class Solution(object):
    def numDecodings(self, s):
        # return zero if there is no input
        # set the dp table
        # initialize the dp table for 2 digit combination
        # update the first digit in dp
        # iterate the dp table
            # accumulate the combinations if the previous single digit is valid
            # accumulate the combinations if the previous two digits are valid 
        # return the final result of the dp table
        pass
```
### Regular Expression Matching
**Recursion**
- [Source code](source/Recursion.py)
```python
class Solution:
    def isMatch(self, text: str, pattern: str) -> bool:
        # return true if all the patterns and the inputs are explored
            # get the result of the validity of the first input
        # if the next pattern is '*'(zero or more repeated)
            # jump over the repeat pattern or check if the next input is repeated
        # if the next pattern is not a repeat
            # check the first input is valid and move to next input and next pattern
        pass
```
**Top Down**
- [Source code](source/TopDown.py)
```python
class Solution(object):
    def dp(self, i, j):
        # if state is not in the cache
            # if current pattern is the last pattern
                # then the current input must be the last input
            # if there are more future patterns
                # get the validation result from the first input
                # if the next pattern is '*'(repeat)
                    # jump over the repeat pattern or check if the next input is repeated
                # if the next pattern is not a repeat
                    # check if the first input is valid and move to next input and next pattern
            # store the result in the cache
        # return the cache
        pass

    def isMatch(self, text, pattern):
        # globlize the inputs
        # create a cache for memoization
        # return the result from the recursion
        pass
```

**Bottom Up**
- [Source code](source/BottomUp.py)
```python
class Solution(object):
    def isMatch(self, text, pattern):
        # create a dp table that uses pattern as column and row as the input
        # set the last pattern and last input as true
        # iterate input backwards 
            # iterate pattern backwards 
                # get the result from the input validation
                # if the next pattern is '*'(repeat)
                    # jump over the repeat pattern or check if the next input is repeated
                # if the next pattern is not a repeat 
                    # check if the first input is valid and move to next input and next pattern
        # return the fully explored result of the dp table
        pass
```
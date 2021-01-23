### Longest Valid Parentheses
**Dynamic Programming**
- [Concepts](images/DP.png)
    - Apply dynamic programming
- [Source code](source/DP.py)
```python
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # set the max length of the parentheses
        # set the dp table 
        # iterate the input 
            # if the current index is a closing
                # if the previous index was a opening 
                    # case1: ( prev ) + ( curr ) 
                # if parentheses exists inside the curr parenthesis   
                    # case2: ( + ( prev ) + )
                # record the max length of the valid parentheses 
        # return the max length of the parentheses 
        pass
```

**Stack**
- [Source code](source/Stack.py)
```python
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # set the maximum length of the parentheses as the return value
        # set a stack 
        # push a sentinel to mark the beginning of the parentheses
        # iterate the input 
            # if the current char is an opening 
                # push the opening to the stack 
            # if the current char is a closing 
                # pop the opening 
                # push the closing as a sentinel if there is no more parenthese 
                # record the max length with the sentinel in the stack
        pass
```

**Without extra space**
- [Source code](source/Space.py)
```python
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # set the index for left, right, and the maximum length
        # iterate the input forward
            # increment left if the char is an opening
            # increment right if the char is an closing
            # record the maximum length of the right if the parentheses is valid 
            # reset the indexes if parenthesis is invalid 
        # reset the indexes for left and right 
        # iterate the input in reverse 
            # increment left if the char is an opening
            # increment right if the char is an closing
            # record the maximum length of the left if the parentheses is valid 
        # return the max length of the parentheses
        pass
```
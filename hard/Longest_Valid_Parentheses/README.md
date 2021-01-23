### Longest Valid Parentheses
**Using Dynamic Programming**
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

**Using Stack**
- [Concepts](images/)
- [Source code](source/)
- [Reference #1]()


**Without extra space**
- [Concepts](images/)
- [Source code](source/)
- [Reference #1]()
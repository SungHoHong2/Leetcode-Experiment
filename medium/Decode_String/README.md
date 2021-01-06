### Decode String
**Using Stack**
- Concepts
    - Use the stack to store the repeated numbers and characters 
- [Stack v2](source/stack2.py)
- [Stack v1](source/stack.py)
```python
"""
  3[a]2[bc]
  stack = [3], curr = a 
  stack = [] curr = aaa
  stack = [2, aaa] curr= bc 
  stack = [] curr= aaa + bcbc
 
  3[2[bc]]
  stack = [3] curr = ''
  stack = [3,2] curr = bc 
  stack = [3] curr = bcbc  
  stack = [] curr = bcbcbcbcbcbc
"""

class Solution:
    def decodeString(self, s: str) -> str:
        # create a stack that stores the current string and the repeated number
        # initialize the pointer of repeat and current string
        # iterate the input
            # if char is part of the repeat number
                # record the repeat considering the number may be two digits (ex 32[a])
            # if the char is an opening bracket
                # save the state of the number of repeats for the current string
                # save the state of the previously created string
                # renew the state of the repeat and the current string
            # if the char is a closing bracket
                # combine the previous result with the repeating current string
            # if char is a data
                # append the char to the current string
        # return the accumulated result
        pass
```

**Using Recursion**
- Concepts 
    - replace the stack with the internal stack used in recursion
- [Source code](source/recursive.py)

```python
class Solution:
    def __init__(self):
        # set the global index
        pass
    
    def decodeString(self, s: str) -> str:
        # set the result string
        # iterate until the input is depleted to the end
            # if the string is a digit
                # compute the repeats
                # ignore the open bracket
                # get the string from recursive operations
                # ignore the closing bracket
                # add the repeated number of strings from the recursive function
            # if the string is not a digit
                # append to the result
                # increase the index
        # return the result
        pass
```

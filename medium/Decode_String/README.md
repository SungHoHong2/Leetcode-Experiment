### Decode String
**Using Stack**
- Concepts
    - Use the stack to store the repeated numbers and characters 
- [Source code](source/stack.py)
```python
class Solution:
    def decodeString(self, s: str) -> str:
        # create a stack that stores the current string and the repeated number
        # intialize the pointer of current string
        # initizlie the pointer of repeated numbers
        # iterate the input
            # if char is the repeat number
                # if the repeat is two digits (ex 32[a])
            # if it is a opening bracket
                # save the state of the previous string
                # save the state for the number of repeats for the current string 
                # set the current string pointer to zero
                # set the repeat pointer to zero
            # if it is a closing bracket
                # pop out the number from the stack
                # pop out the previous string from the stack
                # append the string with the new repeated data
            # if char is a data
                # append the char
        # return the accumulated result
        pass
```

**Using Recursion**
- Concepts 
    - The recursion uses an internal stack to store the previous state.
- [Source code](source/recursive.py)

```python
class Solution:
    # set the global index
    def decodeString(self, s: str) -> str:
        # set the result string
        # iterate until the input is depleted to the end
            # if the string is not a digit
                # append to the result
                # increase the index
            # if the string is a digit
                # get the total number of integers
                # ignore the open bracket
                # get the string from recursive operations
                # ignore the closing bracket
                # add the repeated number of strings from the recursive function
        # return the result
        pass
```

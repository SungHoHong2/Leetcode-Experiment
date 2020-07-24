### Valid Parenthesis

- **Stack**
    - [source code](sources/stack.py)


```python 
class Solution:
    def isValid(self, s: str) -> bool:

        # set up the stack

        # create a hashtable that maps the parenthesis

        # iterate the chars from the string

            # if the char is the closing part of the parenthesis

                # if stack is true then run top_element = stack.pop()
                # if stack is not true then add top_element = '#'

                # if the top element is not the opening part of the parenthesis
                    # return false because it is a unmatching parenthesis


            # if the char is not the closing part of the parenthesis
                # append the stack

        # return true only when the stack is empty
```
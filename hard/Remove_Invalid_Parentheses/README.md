### Remove Invalid Parentheses
**Backtracking**
- [Source code](source/Backtrack.py)
```python
class Solution(object):
    """
    s: the original string we are recursing on
    index: current index in the original string.
    left: number of left parentheses
    right: number of right parentheses
    expr: the resulting expression
    rem_count: number of parentheses that are removed
    """
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def backtrack(index, left, right, expr, removed):
            # reached the end of string
                # if the expression is valid along wit the minimum removal
                    # reset the return array if new minimum number is found
                    # append the string to the return array
                # end the recursion
            # ignore non-parenthesis
            # if the current character is a parenthesis
                # removing one parentheses
                # increment left and move forward if the current parenthesis is an opening bracket
                # increment right and move forward if the current parenthesis is a closing bracket
            pass

        # set a hashset for returning the valid parentheses
        # set a variable to record the minimum removal of parentheses
        # invoke backtrack (s, current index, left, right, expr, removed)
        # return the valid parentheses
        pass
```

**Limited Backtracking**
- [Source code](source/Optimized.py)
```python
class Solution:
    def removeInvalidParentheses(self, s):

        # Find out the number of misplaced left and right parenthesis.
            # record the number of left parenthesis
            # record the number of right parenthesis
                # increment the number of misplaced right if left is zero
                # decrement the number of misplaced left

        def recurse(s, index, left_count, right_count, left_rem, right_rem, expr):
            # if the recursion reached the leaf
                # if the expression is valid
                    # add the answer
            # if the recursion is on progress
                # remove parenthesis only if the misplaced parenthesis exists
                    # remove parenthesis for left or right
                # if the current characetr is not a parenthesis
                # if left parenthesis
                # if right parenthesis and there are more left than right
            pass

        # Run the recursion tree and return the available answers
        pass
```
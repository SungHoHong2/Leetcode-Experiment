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
            if index == len(s):
                # if the expression is valid along wit the minimum removal
                if left == right and removed <= self.min_removed:
                    # reset the return array if new minimum number is found
                    if removed < self.min_removed:
                        self.valid_expressions = set()
                        self.min_removed = removed
                    # append the string to the return array
                    self.valid_expressions.add(expr)
                # end the recursion
                return
            # ignore non-parenthesis
            if s[index] != '(' and s[index] != ')':
                backtrack(index + 1, left, right, expr + s[index], removed)
            # if the current character is a parenthesis
            else:
                # removing one parentheses
                backtrack(index + 1, left, right, expr, removed + 1)
                # increment left and move forward if the current parenthesis is an opening bracket
                if s[index] == '(':
                    backtrack(index + 1, left + 1, right, expr + s[index], removed)
                # increment right and move forward if the current parenthesis is a closing bracket
                elif right < left:
                    backtrack(index + 1, left, right + 1, expr + s[index], removed)

        # set a hashset for returning the valid parentheses
        self.valid_expressions = set()
        # set a variable to record the minimum removal of parentheses
        self.min_removed = float("inf")
        # invoke backtrack (s, current index, left, right, expr, removed)
        backtrack(0, 0, 0, "", 0)
        # return the valid parentheses
        return self.valid_expressions
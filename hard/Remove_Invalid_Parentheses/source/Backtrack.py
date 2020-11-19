class Solution(object):

    def __init__(self):
        self.valid_expressions = None
        self.min_removed = None

    def reset(self):
        self.valid_expressions = set()
        self.min_removed = float("inf")

    """
        string: The original string we are recursing on.
        index: current index in the original string.
        left_count: number of left parentheses till now.
        right_count: number of right parentheses till now.
        expr: the resulting expression in this particular recursion.
        rem_count: number of parentheses ignored in this particular recursion.
    """
    def remaining(self, string, index, left_count, right_count, expr, rem_count):
        # reached the end of string.
        if index == len(string):
            # if the expression is valid along wit the minimum removal
            if left_count == right_count and rem_count <= self.min_removed:
                # reset the return array if new minimum number is found
                if rem_count < self.min_removed:
                    self.valid_expressions = set()
                    self.min_removed = rem_count
                # append the string to the return array
                self.valid_expressions.add(expr)
        # exploring the string
        else:
            # recurse one step ahead if the current character is not a parenthesis
            if string[index] != '(' and  string[index] != ')':
                self.remaining(string, index + 1, left_count, right_count, expr+string[index], rem_count)
            # if the current character is a parenthesis
            else:
                # removing one parenthesis
                self.remaining(string, index + 1, left_count, right_count, expr, rem_count + 1)
                # increment left and move forward if the current parenthesis is an opening bracket
                if string[index] == '(':
                    self.remaining(string, index + 1, left_count + 1, right_count, expr+string[index], rem_count)
                # increment right and move forward if the current parenthesis is a closing bracket
                elif right_count < left_count:
                    self.remaining(string, index + 1, left_count, right_count + 1, expr+string[index], rem_count)

    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # Reset the class level variables that we use for every test case.
        self.reset()
        # Recursive call
        self.remaining(s, 0, 0, 0, "", 0)
        return list(self.valid_expressions)
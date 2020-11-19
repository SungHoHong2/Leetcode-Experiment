class Solution:
    def removeInvalidParentheses(self, s):

        left = 0
        right = 0
        result = set()

        # Find out the number of misplaced left and right parenthesis.
        for char in s:
            # record the number of left parenthesis
            if char == '(':
                left += 1
            elif char == ')':
                # increment the number of misplaced right if left is zero
                right = right + 1 if left == 0 else right
                # decrement the number of misplaced left
                left = left - 1 if left > 0 else left

        def recurse(s, index, left_count, right_count, left_rem, right_rem, expr):

            # if the recursion reached the leaf
            if index == len(s):
                # if the expression is valid
                if left_rem == 0 and right_rem == 0:
                    # add the answer
                    result.add(expr)
                    # result[expr] = 1 # I believe that the result can be a set in this case ...
            else:
                # remove parenthesis only if the misplaced parenthesis exists
                if (s[index] == '(' and left_rem > 0) or (s[index] == ')' and right_rem > 0):
                    # remove parenthesis for left or right
                    recurse(s, index + 1,
                            left_count,
                            right_count,
                            left_rem - (s[index] == '('),
                            right_rem - (s[index] == ')'),
                            expr)
                # if the current characetr is not a parenthesis
                if s[index] != '(' and s[index] != ')':
                    recurse(s, index + 1, left_count, right_count, left_rem, right_rem, expr + s[index])
                # if left parenthesis
                elif s[index] == '(':
                    recurse(s, index + 1,
                            left_count + 1,
                            right_count,
                            left_rem,
                            right_rem, expr + s[index])
                # if right parenthesis and there are more left than right
                elif s[index] == ')' and left_count > right_count:
                    recurse(s, index + 1,
                            left_count,
                            right_count + 1,
                            left_rem,
                            right_rem, expr + s[index])

        # Run the recursion tree and return the available answers
        recurse(s, 0, 0, 0, left, right, "")
        return result

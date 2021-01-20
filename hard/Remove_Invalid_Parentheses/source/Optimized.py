class Solution:
    def removeInvalidParentheses(self, s):

        def backtrack(index, left_count, right_count, left_rem, right_rem, expr):
            # if the recursion explored all the string
            if index == len(s):
                # if the expression is valid
                if left_rem == 0 and right_rem == 0:
                    # add the answer
                    self.result.add(expr)
                # end the recursion
                return
            # remove parenthesis only if the misplaced parenthesis exists
            if (s[index] == '(' and left_rem > 0) or (s[index] == ')' and right_rem > 0):
                # remove parenthesis for left or right
                backtrack(index + 1,
                          left_count,
                          right_count,
                          left_rem - (s[index] == '('),
                          right_rem - (s[index] == ')'),
                          expr)
            # ignore non-parenthesis
            if s[index] != '(' and s[index] != ')':
                backtrack(index + 1,
                          left_count,
                          right_count,
                          left_rem,
                          right_rem,
                          expr + s[index])
            # explore additional left
            elif s[index] == '(':
                backtrack(index + 1,
                          left_count + 1,
                          right_count,
                          left_rem,
                          right_rem,
                          expr + s[index])
            # explore additional right if there are more left than right
            elif s[index] == ')' and left_count > right_count:
                backtrack(index + 1,
                          left_count,
                          right_count + 1,
                          left_rem,
                          right_rem,
                          expr + s[index])

        # find out the number of misplaced left and right parenthesis
        left_rem, right_rem, self.result = 0, 0, set()
        for char in s:
            # record the number of left parenthesis
            if char == '(':
                left_rem += 1
                # record the number of right parenthesis
            elif char == ')':
                # increment the number of misplaced right if there is no more left
                if left_rem == 0:
                    right_rem += 1
                    # decrement the number of misplaced left
                elif left_rem > 0:
                    left_rem -= 1
                    # invoke backtrack
        backtrack(0, 0, 0, left_rem, right_rem, "")
        # return the valid parentheses
        return self.result
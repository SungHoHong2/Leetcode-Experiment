class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # set the maximum length of the parentheses as the return value
        maxLength = 0
        # set a stack
        stack = list()
        # push a sentinel to mark the begining of the parenthese
        stack.append(-1)
        # iterate the input
        for i in range(0, len(s)):
            # if the current char is an opening
            if s[i] == '(':
                # push the opening to the stack
                stack.append(i)
            # if the current char is a closing
            else:
                # pop the opening
                stack.pop()
                # push the closing as a sentinel if there is no more parenthese
                if not stack:
                    stack.append(i)
                # record the max length with the sentinel in the stack
                else:
                    maxLength = max(maxLength, i-stack[-1])
        # return the max length of the parentheses
        return maxLength
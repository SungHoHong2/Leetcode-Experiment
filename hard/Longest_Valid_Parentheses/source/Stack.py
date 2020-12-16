class Solution:
    def longestValidParentheses(self, s: str) -> int:
        maxLength = 0
        stack = list()
        stack.append(-1)
        for i in range(0, len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    maxLength = max(maxLength, i-stack[-1])
        return maxLength
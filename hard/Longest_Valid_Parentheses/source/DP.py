class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # set the max length of the parentheses
        maxLength = 0
        # set the dp table
        dp = [0 for i in s]
        # iterate the input
        for i in range(1, len(s)):
            # if the current index is a closing
            if s[i] == ')':
                # if the previous index was a opening
                if s[i - 1] == '(':
                    # case1: ( prev ) + ( curr )
                    dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
                # if parentheses exists inside the curr parenthesis
                elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == '(':
                    # case2: ( + ( prev ) + )
                    dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2
                # record the max length of the valid parentheses
                maxLength = max(maxLength, dp[i])
        # return the max length of the parentheses
        return maxLength
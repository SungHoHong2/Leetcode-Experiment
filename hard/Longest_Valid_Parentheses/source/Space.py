class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # set the index for left, right, and the maximum length
        left, right, maxLength = 0, 0, 0
        # iterate the input forward
        for i in range(len(s)):
            # increment left if the char is an opening
            if s[i] == '(':
                left += 1
            # increment right if the char is an closing
            else:
                right += 1
            # record the maximum length of the right if the parentheses is valid
            if left == right:
                maxLength = max(maxLength, 2 * right)
            # reset the indexes if parenthesis is invalid
            elif right > left:
                left = right = 0
        # reset the indexes for left and right
        left = right = 0
        # iterate the input in reverse
        for i in range(len(s) - 1, -1, -1):
            # increment left if the char is an opening
            if s[i] == '(':
                left += 1
            # increment right if the char is an closing
            else:
                right += 1
            # record the maximum length of the left if the parentheses is valid
            if left == right:
                maxLength = max(maxLength, 2 * left)
            elif left > right:
                left = right = 0
        # return the max length of the parentheses
        return maxLength


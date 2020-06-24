class Solution:

    def longestPalindrome(self, s: str) -> str:

        if s == None or len(s) < 1:
            return ""

        # initialize the start and the end
        start = 0
        end = 0

        # iterate the string
        for i in range(0, len(s)):

            # in case the total length is odd
            len1 = self.expand(s, i, i)

            # in case the total length is even
            len2 = self.expand(s, i, i + 1)

            # get the longest maxLength
            maxLength = max(len1, len2)
            if maxLength > end - start:
                start = i - (maxLength - 1) // 2
                end = i + maxLength // 2

        # after divided the end will get the lower value
        return s[start:end + 1]

        # expand function

    def expand(self, s, left, right):

        # set up the pointers for left and right
        L = left
        R = right

        # expand until it there is no palindrome
        while L >= 0 and R < len(s) and s[L] == s[R]:
            L -= 1
            R += 1

        # return the length of the palindrome
        return R - L - 1



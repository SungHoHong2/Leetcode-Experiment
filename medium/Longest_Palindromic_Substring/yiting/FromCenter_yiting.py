class Solution(object):
    def ExpandFromCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[right] == s[left]:
            left -= 1
            right += 1
        return s[left + 1:right]

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ''
        for i in range(len(s)):
            result = max(self.ExpandFromCenter(s, i, i), self.ExpandFromCenter(s, i, i + 1), result, key=len)

        return result
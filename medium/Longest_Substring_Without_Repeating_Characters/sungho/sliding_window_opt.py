class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        n = len(s)

        # key = char  value = index of the char
        chkTable = {}

        ans = 0
        i = 0

        for j in range(0, n):

            if s[j] in chkTable:
                i = max(chkTable[s[j]], i)

            ans = max(ans, j - i + 1)
            chkTable[s[j]] = j + 1

        return ans







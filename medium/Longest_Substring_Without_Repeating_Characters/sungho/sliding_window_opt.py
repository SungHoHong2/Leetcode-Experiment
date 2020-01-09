class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        n = len(s)
        chkTable = {}
        ans = i = j = 0

        # i
        #    j
        # abcabcbb
        # 1234

        # (skip)
        #    i
        #    j
        # abcabcbb
        # 1234

        for j in range(0, n):

            # let the (i index) skip all the way to the (j index)
            if s[j] in chkTable:
                i = max(chkTable[s[j]], i)

            ans = max(ans, j - i + 1)
            chkTable[s[j]] = j + 1

            print(ans, j, i)

        return ans


# use HashSet to store the characters in current window [i, j)
# slide the index jj to the right. If it is not in the HashSet, we slide jj further.
# Doing so until s[j] is already in the HashSet.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        n = len(s)
        chkTable = {}
        ans = 0
        i = 0
        j = 0

        # try to extend the range [i,j]
        while i < n and j < n:
            if s[j] not in chkTable:
                chkTable[s[j]] = True
                j += 1
                ans = max(ans, j - i)
            else:
                del chkTable[s[i]]
                i += 1

        return ans



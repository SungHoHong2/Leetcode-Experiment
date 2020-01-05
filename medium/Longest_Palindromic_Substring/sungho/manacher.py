class Solution(object):
    def longestPalindrome(self, s):

        new = "#".join("${}&".format(s))
        n = len(new)
        P = [0 for i in range(n)]
        C = 0
        R = 0

        #   (J)   C   (I)   R
        # ---|----|----|----|---

        for i in range(1, n - 1):
            j = C - (i - C)
            if R - i > P[j]:
                P[i] = P[j]
            else:
                P[i] = R - i

            while new[i + 1 + P[i]] == new[i - 1 - P[i]]:
                P[i] += 1

            if P[i] + i > R:
                R = P[i] + i
                C = i

        l, i = max((l, i) for i, l in enumerate(P))
        return s[(i - l) // 2:(i + l) // 2]
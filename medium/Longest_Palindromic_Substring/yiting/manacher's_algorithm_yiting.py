class Solution:

    def longestPalindrome(self, s: str) -> str:
        new = "#".join("${}&".format(s))
        n = len(new)
        P = [0 for i in range(n)]
        C = 0
        R = 0

        # .    j .   C .    i
        # -----|-----|------|------

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

        length, center = max((l, i) for i, l in enumerate(P))
        return s[(center - length) // 2:(center + length) // 2]










class Solution:

    def longestPalindrome(self, s: str) -> str:

        n = len(s)
        table = [[0 for x in range(0, n)] for y in range(0, n)]
        start = 0
        maxLength = 1

        #     b  a  b  a  d
        #  b [0, 0, 0, 0, 0]
        #  a [0, 0, 0, 0, 0]
        #  b [0, 0, 0, 0, 0]
        #  a [0, 0, 0, 0, 0]
        #  b [0, 0, 0, 0, 0]

        for i in range(0, n):
            table[i][i] = True

        # [True, 0, 0, 0, 0]
        # [0, True, 0, 0, 0]
        # [0, 0, True, 0, 0]
        # [0, 0, 0, True, 0]
        # [0, 0, 0, 0, True]

        for i in range(0, n - 1):
            if s[i] == s[i + 1]:
                table[i][i + 1] = True
                start = i
                maxLength = 2

        for k in range(3, n + 1):
            for i in range(0, n - k + 1):
                j = i + k - 1

                if s[j] == s[i] and table[i + 1][j - 1]:
                    table[i][j] = True
                    start = i
                    maxLength = k

        # i = 0, j = 2, k = 3
        # [True, 0, True, 0, 0]
        # [0, True, 0, 0, 0]
        # [0, 0, True, 0, 0]
        # [0, 0, 0, True, 0]
        # [0, 0, 0, 0, True]


        # i = 1, j = 3, k = 3
        # [True, 0, True, 0, 0]
        # [0, True, 0, True, 0]
        # [0, 0, True, 0, 0]
        # [0, 0, 0, True, 0]
        # [0, 0, 0, 0, True]

        # i = 2, j = 4, k = 3
        # [True, 0, True, 0, 0]
        # [0, True, 0, True, 0]
        # [0, 0, True, 0, 0]
        # [0, 0, 0, True, 0]
        # [0, 0, 0, 0, True]

        # i = 0, j = 3, k = 4
        # [True, 0, True, 0, 0]
        # [0, True, 0, True, 0]
        # [0, 0, True, 0, 0]
        # [0, 0, 0, True, 0]
        # [0, 0, 0, 0, True]

        # i = 1, j = 4, k = 4
        # [True, 0, True, 0, 0]
        # [0, True, 0, True, 0]
        # [0, 0, True, 0, 0]
        # [0, 0, 0, True, 0]
        # [0, 0, 0, 0, True]

        # i = 0. j = 4, k = 5
        # [True, 0, True, 0, 0]
        # [0, True, 0, True, 0]
        # [0, 0, True, 0, 0]
        # [0, 0, 0, True, 0]
        # [0, 0, 0, 0, True]

        return s[start: start + maxLength]
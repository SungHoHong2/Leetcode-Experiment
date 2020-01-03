class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)  # get length of input string

        table = [[0 for x in range(n)] for y in range(n)]

        # for i in table:
        #     print(i)

        maxLength = 1
        i = 0
        while i < n:
            table[i][i] = True
            i += 1

        #         for i in table:
        #             print(i)

        start = 0
        i = 0
        while i < n - 1:
            if s[i] == s[i + 1]:
                table[i][i + 1] = True
                start = i
                maxLength = 2
            i = i + 1

        k = 3
        while k <= n:
            i = 0
            while i < (n - k + 1):
                j = i + k - 1

                if table[i + 1][j - 1] and s[i] == s[j]:
                    table[i][j] = True

                    if (k > maxLength):
                        start = i
                        maxLength = k

                        # print(i,j)

                i += 1
            k += 1

        return s[start:start + maxLength]

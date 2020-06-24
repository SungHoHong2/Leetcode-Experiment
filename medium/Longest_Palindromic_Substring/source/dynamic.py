class Solution:

    def longestPalindrome(self, s: str) -> str:

        # construct the matrix of dp

        #     b  a  b  a  d
        #  b [0, 0, 0, 0, 0]
        #  a [0, 0, 0, 0, 0]
        #  b [0, 0, 0, 0, 0]
        #  a [0, 0, 0, 0, 0]
        #  b [0, 0, 0, 0, 0]

        n = len(s)
        table = [[0 for x in range(0, n)] for y in range(0, n)]
        start = 0
        maxLength = 1

        # create true for the cells positioned diagonally
        for i in range(0, n):
            table[i][i] = True

        # update true for neighboring cells
        for i in range(0, n - 1):
            if s[i] == s[i + 1]:
                table[i][i + 1] = True
                start = i
                maxLength = 2

        # update true for cells that represent palindrome larger than 3

        # palindrome size from 3 to totalarray k = (n+1)
        for k in range(3, n + 1):

            # starting point of the substring
            for i in range(0, n - k + 1):

                # end point of substring
                j = i + k - 1

                # if cells from i and j are equal and the history is true
                if s[j] == s[i] and table[i + 1][j - 1]:
                    table[i][j] = True
                    start = i
                    maxLength = k

        # return the result
        return s[start: start + maxLength]
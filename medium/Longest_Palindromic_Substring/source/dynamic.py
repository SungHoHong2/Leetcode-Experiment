class Solution:
    def longestPalindrome(self, s: str) -> str:
        # construct the matrix of dp
        #     b  a  b  a  d
        #  b [0, 0, 0, 0, 0]
        #  a [0, 0, 0, 0, 0]
        #  b [0, 0, 0, 0, 0]
        #  a [0, 0, 0, 0, 0]
        #  b [0, 0, 0, 0, 0]
        # create the table
        table = [[0 for x in range(len(s))] for y in range(len(s))]
        # set the start variable
        start = 0
        # check for palindromes with the length of 1
        maxLength = 1
        for i in range(0, len(s)):
            table[i][i] = True
        # check for palindromes with the length of 2
        for i in range(0, len(s)-1):
            if s[i] == s[i + 1]:
                table[i][i+1] = True
                start = i
                maxLength = 2
        # check for palindromes with the length larger than 3
        for k in range(3, len(s)+1):
            for i in range(0, len(s)-k+1):
                j = i + k - 1
                 # if cells from i and j are equal and the history is true
                if s[j] == s[i] and table[i+1][j-1]:
                    table[i][j] = True
                    start = i
                    maxLength = k
        # return the result
        return s[start: start + maxLength]
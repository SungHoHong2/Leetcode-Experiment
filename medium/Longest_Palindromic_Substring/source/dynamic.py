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
        table = [[0 for i in s] for j in s]
        # set the start variable
        start = 0
        # set the maximum length of the palindrome
        maxLength = 1
        # check the palindrome of a single character
        for i in range(len(s)):
            # compare with itself
            table[i][i] = True
        # check the palindrome of a neighboring character
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                table[i][i+1] = True
                start = i
                maxLength = 2
        # check the palindrome that has the size from 3 to n
        for k in range(3, len(s)+1):
            # starting point of the substring (make sure n-k != 0)
            for i in range(len(s)-k+1):
                # end point of substring (make sure k < len(s))
                j = i + k - 1
                # if cells from i and j are equal and the history is true
                if s[i] == s[j] and table[i+1][j-1]:
                    table[i][j] = True
                    start = i
                    maxLength = k
        # return the result
        return s[start:start+maxLength]
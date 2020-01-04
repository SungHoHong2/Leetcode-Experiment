class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        n = len(s)
        start = 0
        maxl = 1
        arr = [[0 for x in range(n)] for y in range(n)]

        for i in range(n):
            arr[i][i] = True

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                arr[i][i + 1] = True
                start = i
                maxl = 2

        step = 3

        for step in range(3, n + 1):
            for i in range(0, n - step + 1):
                j = i + step - 1
                if s[i] == s[j] and arr[i + 1][j - 1] == True:
                    arr[i][j] = True
                    if step > maxl:
                        start = i
                        maxl = step

        return s[start:start + maxl]
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if s == "":
            return 0
        p = 1
        pp = 0

        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                cur = 0
            else:
                cur = p
            if i + 1 < n and (s[i] == '1' or (s[i] == '2' and s[i + 1] < '7')):
                cur += pp
            pp = p
            p = cur

        return p
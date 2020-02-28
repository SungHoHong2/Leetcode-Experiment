class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        def helper(k, s):
            if k == len(s):
                return 1
            if s[k] == "0":
                return 0
            res = helper(k + 1, s)
            if k < len(s) - 1 and (s[k] == '1' or (s[k] == '2' and s[k + 1] < '7')):
                res += helper(k + 2, s)
            return res

        if s == "":
            return 0
        return helper(0, s)

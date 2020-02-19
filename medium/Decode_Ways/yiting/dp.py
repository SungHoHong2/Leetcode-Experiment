class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        if s[0] != '0':
            dp[1] = 1
        else:
            dp[1] = 0
        for i in range(2, len(s) + 1):

            first = int(s[i - 1:i])
            second = int(s[i - 2:i])
            if 0 < first < 10:
                dp[i] += dp[i - 1]
            if 9 < second < 27:
                dp[i] += dp[i - 2]

        return dp[len(s)]
class Solution(object):
    def numDecodings(self, s):
        # return zero if there is no input
        if not s:
            return 0
        # set the dp table
        dp = [0 for _ in range(len(s) + 1)]
        # initalize the dp table for 2 digit combination
        dp[0] = 1
        # update the first digit in dp
        dp[1] = 0 if s[0] == '0' else 1
        # iterate the input
        for i in range(2, len(dp)):
            # accumulate the combinations if the previous single digit is valid
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            # accumulate the combinations if the previous two digits are valid
            two_digit = int(s[i-2 : i])
            if 10 <= two_digit <= 26:
                dp[i] += dp[i-2]
        # return the final result of the dp list
        return dp[len(s)]
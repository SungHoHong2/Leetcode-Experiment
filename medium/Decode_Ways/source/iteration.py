class Solution(object):
    def numDecodings(self, s):
        # if there is no input
        if not s:
            # return zero
            return 0
        # set the list to store the subproblem results
        dp = [0 for _ in range(len(s) + 1)]
        # initialize the list
        dp[0] = 1
        # update the first number to 1 unless it is a zero
        dp[1] = 0 if s[0] == '0' else 1
        # record all the subproblem results
        for i in range(2, len(dp)):
            # if the number is not a zero
            if s[i-1] != '0':
                # accumulate the number to the dp list
                dp[i] += dp[i-1]
            # get the two digit number
            two_digit = int(s[i-2 : i])
            # if the two digit number is a valid number
            if 10 <= two_digit <= 26:
                # accumulate the number to the dp list
                dp[i] += dp[i-2]
        # return the final result of the dp list
        return dp[len(s)]
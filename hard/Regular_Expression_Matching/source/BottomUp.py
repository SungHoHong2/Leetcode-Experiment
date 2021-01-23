class Solution(object):
    def isMatch(self, text, pattern):
        # create a dp table that uses pattern as column and row as the input
        dp = [[False for _ in range(len(pattern) + 1)] for _ in range(len(text) + 1)]
        # set the last pattern and last input as true
        dp[-1][-1] = True
        # iterate input backwards
        for i in range(len(text), -1, -1):
            # iterate pattern backwards
            for j in range(len(pattern)-1, -1, -1):
                # get the result from the input validation
                match = i < len(text) and pattern[j] in {text[i], '.'}
                # if the next pattern is '*'(repeat)
                if j+1 < len(pattern) and pattern[j+1] == '*':
                    # jump over the repeat pattern or check if the next input is repeated
                    dp[i][j] = dp[i][j+2] or match and dp[i+1][j]
                # if the next pattern is not a repeat
                else:
                    # check if the first input is valid and move to next input and next pattern
                    dp[i][j] = match and dp[i+1][j+1]
        # return the fully explored result of the dp table
        return dp[0][0]
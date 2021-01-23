class Solution(object):
    def topdown(self, i, j):
        # if state is not in the cache
        if not self.dp[i][j]:
            # if current pattern is the last pattern
            if j == len(self.pattern):
                # then the current input must be the last input
                ans = i == len(self.text)
            # if there are more future patterns
            else:
                # get the validation result from the first input
                match = i < len(self.text) and self.pattern[j] in {self.text[i], '.'}
                # if the next pattern is '*'(repeat)
                if j + 1 < len(self.pattern) and self.pattern[j + 1] == '*':
                    # jump over the repeat pattern or check if the next input is repeated
                    ans = self.topdown(i, j + 2) or match and self.topdown(i + 1, j)
                # if the next pattern is not a repeat
                else:
                    # check if the first input is valid and move to next input and next pattern
                    ans = match and self.topdown(i + 1, j + 1)
            # store the result in the cache
            self.dp[i][j] = ans
        # return the cache
        return self.dp[i][j]

    def isMatch(self, text, pattern):
        # globlize the inputs
        self.text, self.pattern = text, pattern
        # set a dp table
        self.dp = [[False for _ in range(len(pattern) + 1)] for _ in range(len(text) + 1)]
        # return the result from the recursion
        return self.topdown(0,0)
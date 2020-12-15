class Solution(object):
    def dp(self, i, j):
        # if state is not in the cache
        if (i, j) not in self.cache:
            # if current pattern is the last pattern
            if j == len(self.pattern):
                # then the current input must be the last input
                ans = i == len(self.text)
            # if there are more future patterns
            else:
                # get the validation result from the first input
                first_match = i < len(self.text) and self.pattern[j] in {self.text[i], '.'}
                # if the next pattern is '*'(repeat)
                if j + 1 < len(self.pattern) and self.pattern[j + 1] == '*':
                    # jump over the repeat pattern or check if the next input is repeated
                    ans = self.dp(i, j + 2) or first_match and self.dp(i + 1, j)
                # if the next pattern is not a repeat
                else:
                    # check if the first input is valid and move to next input and next pattern
                    ans = first_match and self.dp(i + 1, j + 1)
            # store the result in the cache
            self.cache[i, j] = ans
        # return the cache
        return self.cache[i, j]

    def isMatch(self, text, pattern):
        # globlize the inputs
        self.text, self.pattern = text, pattern
        # create a cache for memoization
        self.cache = dict()
        # return the result from the recursion
        return self.dp(0, 0)
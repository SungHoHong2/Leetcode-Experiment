class Solution:
    def __init__(self):
        # set a map to record the possible characters
        self.dp = dict()

    def recursive(self, index, s) -> int:
        # return 1 if the last two digits are valid
        if index == len(s):
            return 1
        # return 0 if the last single digit is zero (invalid)
        if s[index] == '0':
            return 0
        # return 1 if the last single digit is valid
        if index == len(s)-1 :
            return 1
        # return the cached result if the rightside of the digits are visited
        if index in self.dp:
            return self.dp[index]
        # get the combinations from a single digit
        ans = self.recursive(index+1, s)
        # get the combinations from a double digit if it is valid
        ans += self.recursive(index+2, s) if int(s[index : index+2]) <= 26 else 0
        # record the possible combinations for the current digit
        self.dp[index] = ans
        # return the result
        return self.dp[index]

    def numDecodings(self, s: str) -> int:
        # return 0 if there is no input
        if not s:
            return 0
        # invoke the recursion
        return self.recursive(0, s)
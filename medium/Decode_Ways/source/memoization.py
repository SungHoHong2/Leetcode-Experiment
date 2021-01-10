class Solution:

    def recursive(self, index, s) -> int:
        # return 1 if the last two digits are valid
        if index == len(s):
            return 1
        # return 0 if the last single digit is zero (invalid)
        if int(s[index]) == 0:
            return 0
        # return 1 if the last single digit is valid
        if index == len(s) - 1:
            return 1
        # return the cached result if the rightside of the digits are visited
        if self.dp[index] :
            return self.dp[index]
        # get the combinations from a single digit
        ans = self.recursive(index+1, s)
        # get the combinations from a double digit if it is valid
        ans += self.recursive(index+2, s) if 10<= int(s[index:index+2]) <= 26 else 0
        # record the possible combinations for the current digit
        self.dp[index] = ans
        # return the result
        return ans

    def numDecodings(self, s: str) -> int:
        # return 0 if there is no input
        if not s:
            return 0
        # set the dp table to record the possible characters
        self.dp = [0 for i in range(len(s)-1)]
        # invoke the recursion
        return self.recursive(0, s)
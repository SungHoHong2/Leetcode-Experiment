class Solution:

    def helper(self, data, k, memo):
        if k == 0:
            return 1

        # the starting point
        s = len(data) - k

        # if there is zero at the first element return nothing
        if data[s] == '0':
            return 0

        if memo[k] is not None:
            return memo[k]

        # move one one step forward
        result = self.helper(data, k - 1, memo)

        # move two step forward if the two numbers are below 26
        if k >= 2 and int(data[s:s + 2]) <= 26:
            result += self.helper(data, k - 2, memo)

        memo[k] = result

        # keep aggregating the result
        return result

    def numDecodings(self, s):
        memo = [None for i in range(len(s) + 1)]
        return self.helper(s, len(s), memo)








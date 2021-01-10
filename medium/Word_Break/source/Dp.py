class Solution(object):
    def wordBreak(self, s, wordDict):
        # set up the dp table
        dp = [False for _ in s]
        # iterate the string
        for end in range(len(s)):
            # interate the substring backwards
            for start in range(end+1,-1,-1):
                # if the current word is valid and the previous substrings are valid
                if s[start:end+1] in wordDict and (dp[start-1] if start > 0 else True):
                    # set the dp table to true
                    dp[end] = True
                    # ignore the rest of the substrings
                    break
        # return the final result of the record
        return dp[len(s)-1]
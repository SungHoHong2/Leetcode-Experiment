class Solution(object):
    def wordBreak(self, s, wordDict):
        # set up the dp table
        dp = [False for _ in s]
        # iterate the string
        for end in range(1,len(s)+1):
            # iterate the substring backwards
            for start in range(end, -1, -1):
                # if the current word is valid and the previous substrings are valid
                if s[start:end] in wordDict and (dp[start-1] if start > 0 else True):
                    # set the dp table to true
                    dp[end-1] = True
                    # ignore the rest of the substrings
                    break
        # return the final result of the record
        return dp[len(s)-1]
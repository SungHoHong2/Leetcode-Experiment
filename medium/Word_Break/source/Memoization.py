class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # create a list that will be used for memoization
        dp = [None for _ in s]
        # set the inputs as global
        self.s, self.wordDict = s, wordDict
        # invoke the recursion
        return self.recursion(0, dp)

    def recursion(self, start, dp):
        # return true if the recursion reaches the leaf
        if start == len(self.s):
            return True
        # return the record if a record is found
        if dp[start] != None:
            return dp[start]
        # iterate from start to the end
        for end in range(start+1, len(self.s)+1):
            # if the substring matches with the wordDict and recursion no mismatches afterwards
            if self.s[start:end] in self.wordDict and self.recursion(end, dp):
                # record the result as true
                dp[start] = True
                # return True
                return True
        # if nothing found cache the memo with False
        dp[start] = False
        # return False
        return False

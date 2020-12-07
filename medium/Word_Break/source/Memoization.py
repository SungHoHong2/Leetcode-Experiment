class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # create a list of to record the results of the substring
        memo = [None for i in s]
        # set the inputs as global
        self.s, self.wordDict = s, wordDict
        # invoke the recursion
        return self.bruteBreak(0, memo)

    def bruteBreak(self, start, memo):
        # return true if the recursion reaches the leaf
        if start == len(self.s):
            return True
        # return the record if a record is found
        if memo[start] != None:
            return memo[start]
        # iterate from start to the end
        for end in range(start+1, len(self.s) + 1):
            # if the substring matches with the wordDict and recursion no mismatches afterwards
            if self.s[start:end] in self.wordDict and self.bruteBreak(end, memo):
                # record the result as true
                memo[start] = True
                # return True
                return memo[start]
        # if nothing found cache the memo with False
        memo[start] = False
        # return False
        return memo[start]
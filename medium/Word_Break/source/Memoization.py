class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # create a list of to record the results of the substring
        memo = [None for i in range(len(s))]
        # invoke the recursion
        return self.bruteBreak(s, set(wordDict), 0, memo)

    def bruteBreak(self, s, wordDict, start, memo):
        # if the recursion reaches the leaf
        if start == len(s):
            # return as True
            return True
        # if a record is found
        if memo[start] != None:
            # return the result from the record
            return memo[start]

        # iterate from start to the end
        for end in range(start + 1, len(s) + 1):
            # if the substring matches with the wordDict and recursion no mismatches afterwards
            if s[start:end] in wordDict and self.bruteBreak(s, wordDict, end, memo):
                # record the result as true
                memo[start] = True
                # return True
                return memo[start]
        # if nothing found cache the memo with False
        memo[start] = False
        # return False
        return memo[start]
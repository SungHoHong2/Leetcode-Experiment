class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # create a list of memo
        memo = [None for i in range(len(s))]
        # call the recursive function (s, wordDict as set, start, memo)
        return self.bruteBreak(s, set(wordDict), 0, memo)

    # recursive function
    def bruteBreak(self, s, wordDict, start, memo):

        # if the starting point equals to length
        if start == len(s):
            # return as True
            return True

            # if there is a memo
        if memo[start] != None:
            # return the result from the memo
            return memo[start]

        # iterate from start to the end
        for end in range(start + 1, len(s) + 1):
            # if the substring matches with the wordDict and recursive function returns True
            if s[start:end] in wordDict and self.bruteBreak(s, wordDict, end, memo):
                # cache the memo with True
                memo[start] = True
                # return True
                return memo[start]

        # if nothing found cache the memo with False
        memo[start] = False
        # return False
        return memo[start]
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        memo = [None for i in range(len(s))]
        return self.bruteBreak(s, set(wordDict), 0, memo)

    def bruteBreak(self, s, wordDict, start, memo):

        print(start, s[start:len(s)])

        if start == len(s):
            return True

        if memo[start] != None:
            return memo[start]

        for end in range(start + 1, len(s) + 1):
            if s[start:end] in wordDict and self.bruteBreak(s, wordDict, end, memo):
                memo[start] = True
                return memo[start]

        memo[start] = False
        return memo[start]

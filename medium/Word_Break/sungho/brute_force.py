class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        return self.bruteBreak(s, set(wordDict), 0)

    def bruteBreak(self, s, wordDict, start):

        if start == len(s):
            return True

        for end in range(start + 1, len(s) + 1):
            if s[start:end] in wordDict and self.bruteBreak(s, wordDict, end):
                return True

        return False

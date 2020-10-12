class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # invoke recursion
        return self.bruteBreak(s, set(wordDict), 0)

    def bruteBreak(self, s, wordDict, start):
        # if the recursion checked the entire input
        if start == len(s):
            # return true
            return True
        for end in range(start + 1, len(s) + 1):
            # check if the substring is part of the word dictionary and run the recursion after the substring
            if s[start:end] in wordDict and self.bruteBreak(s, wordDict, end):
                # if substring is part of dictionary and there are no mismatches afterwards
                return True
        # return false if there is a mismatch or a substring that is not part of the dictionary
        return False

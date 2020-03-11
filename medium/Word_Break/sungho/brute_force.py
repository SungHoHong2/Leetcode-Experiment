class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        return self.helper(0, s, wordDict, {})

    def helper(self, k, s, wordDict, cache):
        if k == len(s):
            return True
        elif k in cache:
            return cache[k]
        else:
            for i in range(k, len(s)):
                if s[k:i + 1] in wordDict:
                    if self.helper(i + 1, s, wordDict, cache):
                        cache[k] = True
                        return True
        cache[k] = False
        return cache[k]








class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        table = [False]*(len(s))
        for j in range(len(s)):
            for i in range(j, -1, -1):
                word_so_far = s[i:j+1]
                left_is_breakable = table[i-1] if i > 0 else True
                if word_so_far in wordDict and left_is_breakable:
                    table[j] = True
                    break
        return table[-1]
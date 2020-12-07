class Solution(object):
    def wordBreak(self, s, wordDict):
        # set up the dp table
        table = [False for i in s]
        # iterate the string
        for j in range(len(s)):
            # interate the substring backwards
            for i in range(j, -1, -1):
                # if the current word is valid and the previous substrings are valid
                if s[i:j+1] in wordDict and (table[i-1] if i > 0 else True):
                    # return true
                    table[j] = True
                    # no need to check the rest of the substrings
                    break
        # return the final result of the record
        return table[len(s)-1]

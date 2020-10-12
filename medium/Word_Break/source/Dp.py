class Solution(object):
    def wordBreak(self, s, wordDict):
        # set up a list to record the substrings
        table = [False]*(len(s))
        # iterate the string
        for j in range(len(s)):
            # interate the substring backwards
            for i in range(j, -1, -1):
                # get teh sbustring
                word_so_far = s[i:j+1]
                # check the validity of the previous substring
                left_is_breakable = table[i-1] if i > 0 else True
                # if the current word is valid and the previous substrings are valid
                if word_so_far in wordDict and left_is_breakable:
                    # return true
                    table[j] = True
                    # no need to check the rest of the substrings
                    break
        # return the final result of the record
        return table[-1]
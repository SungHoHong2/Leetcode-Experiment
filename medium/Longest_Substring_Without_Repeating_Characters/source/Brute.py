class Solution:
    def allUnique(self, s, start, end):
        # setup a hashset
        check = set()
        # iterate from start
        for i in range(start, end):
            # if duplicate is found
            if s[i] in check:
                # return false
                return False
            # record the characters in the hashmap
            check.add(s[i])
        # return true if there is no duplicate found
        return True

    def lengthOfLongestSubstring(self, s: str) -> int:
        # set the return value
        ans = 0
        # iterate the entire string twice
        for i in range(0, len(s)):
            for j in range(i + 1, len(s) + 1):
                # check for duplicated characters
                if self.allUnique(s, i, j):
                    # if the characters are unique update the answer
                    ans = max(ans, j - i)
        # return the answer
        return ans
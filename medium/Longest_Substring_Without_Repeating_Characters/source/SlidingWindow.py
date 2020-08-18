class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # set a hashset
        hashset = set()
        # set the return variable
        ans = i = j = 0
        # loop until start or end exceeds the limit
        while i < len(s) and j < len(s):
            # if end pointer is unique
            if s[j] not in hashset:
                # record the end character in the hashset
                hashset.add(s[j])
                # increase the end pointer
                j += 1
                # record the maximum return value
                ans = max(ans, j - i)
            # if the right pointer is a duplicate
            else:
                # remove the the start character from the hashset
                hashset.remove(s[i])
                # increase the start pointer
                i += 1
        # return the answer
        return ans

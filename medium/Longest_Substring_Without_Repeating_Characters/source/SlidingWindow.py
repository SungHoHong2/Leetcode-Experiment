class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # set a hashset
        hashset = set()
        # set the return variable
        ans = start = end = 0
        # loop until start or end exceeds the limit
        while start < len(s) and end < len(s):
            # if end pointer is unique
            if s[end] not in hashset:
                # record the end character in the hashset
                hashset.add(s[end])
                # increase the end pointer
                end += 1
                # record the maximum return value
                ans = max(ans, end - start)
            # if the right pointer is a duplicate
            else:
                # remove the the start character from the hashset
                hashset.remove(s[start])
                # increase the start pointer
                start += 1
        # return the answer
        return ans

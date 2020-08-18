class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # set a hashset
        hashmap = dict()
        # set the return variable
        ans = start = end = 0
        # loop until the end exceeds the limit
        while end < len(s):
            # if the end character is a duplicate
            if s[end] in hashmap:
                # move the start to the duplicated character
                start = max(hashmap[s[end]], start)
            # increment the end pointer
            end += 1
            # update the maximum length
            ans = max(ans, end-start)
            # record the duplicated character with the future starting point
            hashmap[s[end-1]] = end
        # return the answer
        return ans

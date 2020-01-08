class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        j = 0
        result = 0
        check = set()
        while i < len(s) and j < len(s):
            if s[j] not in check:
                check.add(s[j])
                result = max(result, j - i + 1)
                j += 1
            else:
                check.remove(s[i])
                i += 1

        return result



class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = ""
        tmp = ""
        maxl = 0
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        for i in range(len(s)):

            if s[i] not in tmp:

                tmp += s[i]
                if len(tmp) > maxl:
                    maxl = len(tmp)
                    result = tmp
            else:
                n = tmp.index(s[i])
                if n == len(tmp) - 1:
                    tmp = s[i]
                else:
                    tmp = tmp[n + 1:] + s[i]

        return len(result)

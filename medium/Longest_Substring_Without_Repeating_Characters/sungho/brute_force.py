class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Given a string, find the length of the longest substring without repeating characters.

        def allUnique(s, start, end):

            # print(start, end)
            check = {}
            for i in range(start, end):
                ch = s[i]
                # print(ch, ch in check)
                if ch in check:
                    return False

                check[ch] = True
            return True

        n = len(s)
        ans = 0

        for i in range(0, n):
            for j in range(i + 1, n + 1):
                if allUnique(s, i, j):
                    ans = max(ans, j - i)

        return ans




class Solution:

    # function that checks whether the specified range is a palindrome
    def isPaindrome(self, s, i, j):
        for k in range(i, j):
            if s[k] != s[j - k + i]:
                return False

        return True

    def validPalindrome(self, s: str) -> bool:

        # iterate only half the string
        for i in range(len(s) // 2):
            # if the start and the end of the string are not equal
            j = len(s) - 1 - i
            if s[i] != s[j]:
                return self.isPaindrome(s, i + 1, j) or self.isPaindrome(s, i, j - 1)

        # every string from start to the end are equal
        return True

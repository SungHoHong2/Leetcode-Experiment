class Solution:
    def longestPalindrome(self, s: str) -> str:
        # initialize the start and the end
        start = end = 0
        # iterate the string
        for i in range(0, len(s)):
            # in case the total length is odd
            len1 = self.expand(s,i,i)
            # in case the total length is even
            len2 = self.expand(s, i, i+1)
            # get the longest maxLength
            maxLength  = max(len1, len2)
            # if the maxlength hits the record
            if maxLength > end - start:
                # update the start and end variable
                start = i - (maxLength-2) // 2
                end = i + (maxLength+1) // 2
        # after divided return the substring result
        return s[start:end]
    # function that returns the largest length of the palindrome
    def expand(self, arr, left, right):
        # set up the pointers for left and right
        L = left
        R = right
        # expand until it there is no palindrome
        while L >=0 and R < len(arr) and arr[L] == arr[R]:
            L -= 1
            R += 1
        # return the length of the palindrome
        return R - L
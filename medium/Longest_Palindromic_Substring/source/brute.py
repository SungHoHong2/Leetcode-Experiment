class Solution:
    # function for checking the largest palindrome
    def palindrome(self, arr, index):
        # set the variables for the odd palindrome
        left = index - 1
        right = index + 1
        odd = 0
        # loop until the palindrome is invalid
        while left >= 0 and right < len(arr) and arr[left] == arr[right]:
            # increase the size of the odd paliindrome
            odd += 1
            # increase the left and right index
            left -= 1
            right += 1
            # set the variables for the even palindrome
        left = index - 1
        right = index
        even = 0
        # loop until the palindrome is invalid
        while left >= 0 and right < len(arr) and arr[left] == arr[right]:
            even += 1
            left -= 1
            right += 1
            # return the largest odd or even palindrome
        return (index - odd, index + odd) if odd >= even else (index - even, index + even - 1)

    def longestPalindrome(self, s: str) -> str:
        # set the variable for the largest substring
        maxString = ""
        # if the string is less than equal to one
        if len(s) <= 1 :
            # return the original input
            return s
        # iterate the string
        for i in range(1, len(s)):
            # invoke palindrome checker and get the left and right index
            left, right = self.palindrome(s, i)
            # if the length of the substring creates a new record
            if len(maxString) < len(s[left:right + 1]):
                # update the largest substring
                maxString = s[left:right + 1]
        # return the largest substring
        return maxString




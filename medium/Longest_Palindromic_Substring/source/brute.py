class Solution:
    # function for checking the largest palindrome
    def chkPalindrome(self, arr, index):
        # set the left and right index for the odd palindrome
        left = index - 1
        right = index + 1
        # set the variable for the largest odd palindrome
        oddLength = 0
        # loop until left and right reach the end
        while left >=0 and right < len(arr):
            # if it is a plaindrome
            if arr[left] == arr[right]:
                # increase the size of the odd paliindrome
                oddLength += 1
            # if it is not a palindrome
            else:
                # escape the loop
                break
            # increase the left and right index
            left -= 1
            right += 1
        # left and right index for the even palindrome
        left = index - 1
        right = index
        # find the even palindrome using the same method of finding the odd palindrome
        evenLength = 0
        # if odd palindrome is larger
        while left >= 0 and right < len(arr):
            # return the index for the odd palindrome
            if arr[left] == arr[right]:
                evenLength += 1
            else:
                break
            left -= 1
            right += 1
        # if even palindrome is larger
        if oddLength >= evenLength:
            return index - oddLength, index+ oddLength
        else:
            # return the index for the even palindrome and note that even has no centerpoint
            return index - evenLength, index + evenLength - 1

    def longestPalindrome(self, s: str) -> str:
        # set the variable for the largest substring
        maxString = ""
        # if the string is none
        if len(s) == 0 or len(s) == 1:
            # return empty string
            return s
        # iterate the string
        for i in range(1, len(s)):
            # invoke palindrome checker and get the left and right index
            left, right = self.chkPalindrome(s,i)
            # if the length of the substring creates a new record
            if len(maxString) < len(s[left:right+1]):
                # update the largest substring
                maxString = s[left:right+1]
        # return the largest substring
        return maxString
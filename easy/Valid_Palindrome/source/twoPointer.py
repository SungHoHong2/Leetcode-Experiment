class Solution:
    def isPalindrome(self, s: str) -> bool:
        # set the two pointers for the start and the end
        i, j = 0, len(s) - 1
        # loop until the two pointers converge
        while i < j:
            # if the two pointers did not converge and the start is not a number or character
            while i < j and not(s[i].isalpha() or s[i].isnumeric()):
                # skip
                i += 1
            # if the two pointers did not converge and the end is not a number or character
            while i < j and not(s[j].isalpha() or s[j].isnumeric()):
                # skip
                j -= 1
            # if the start and the end are not identical
            if s[i].lower() != s[j].lower():
                # return false
                return False
            # decrease the distance between start and end
            i += 1
            j -= 1
        # if no problem detected then it is a palindrome
        return True
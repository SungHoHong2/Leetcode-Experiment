class Solution:
    def isPalindrome(self, s: str) -> bool:
        # convert the argument into a lower letter containing only characters or numbers
        result = list([val for val in s.lower() if val.isalpha() or val.isnumeric()])
        # compare the resulting array with the reversed array
        if result == result[::-1]:
            return True
        else:
            return False

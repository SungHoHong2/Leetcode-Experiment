class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = list([val for val in s.lower() if val.isalpha() or val.isnumeric()])

        # print(result, result[::-1])
        if result == result[::-1]:
            return True
        else:
            return False


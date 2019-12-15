class Solution:
    def isPalindrome(self, x: int) -> bool:

        # Special cases:
        # 1. As discussed above, when x < 0, x is not a palindrome.
        # 2. if the last digit of the number is 0, in order to be a palindrome,
        #    the first digit of the number also needs to be 0.
        # Only 0 satisfy this property.

        # Only zero satisfy
        if x < 0 or (x % 10 == 0 and x != 0):
            return False;

        revertedNumber = 0
        original = x

        while int(x) != 0:
            revertedNumber = revertedNumber * 10 + int(x % 10)
            # print(revertedNumber, int(x%10))
            x /= 10

        # print(revertedNumber, int(x), int(x%10))
        return original == revertedNumber








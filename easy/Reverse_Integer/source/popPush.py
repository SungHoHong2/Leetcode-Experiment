class Solution:
    def reverse(self, x: int) -> int:
        # set return value
        res = 0
        # set a flag for checking negative number
        negative = False
        # if the arguement is a negative number
        if x < 0:
            # set the flag as true
            negative = True
            # modify the arguement to positive number
            x *= -1
            # iterate until the arguement is depleted
        while x != 0:
            # push the number from right to left
            res = res * 10 + x % 10
            # reduce the number from left to right
            x = x // 10

            # if the number is out side the scope of the integer
        if res > pow(2, 31) - 1:
            # return zero
            return 0
        # if the original argument was negative
        if negative:
            # covert the return value back to negative number
            res *= -1
            # return the result
        return res
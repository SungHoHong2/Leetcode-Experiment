class Solution:
    def reverse(self, x: int) -> int:

        res = 0
        negative = False

        if x < 0:
            negative = True
            x *= -1

        while x != 0:
            res = res * 10 + x % 10
            x = int(x / 10)
            # print(x)

        if res > (2 ** 31 - 1):
          
            return 0

        if negative:
            res *= -1

        return res
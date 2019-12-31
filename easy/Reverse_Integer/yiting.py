class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = 0
        negative = x < 0
        x = abs(x)
        while x != 0:
            remain = x % 10
            x = x / 10
            result = result * 10 + remain

        if result >= 2 ** 31:
            return 0
        if result < -2 ** 31:
            return 0
        if negative:
            return result * -1
        return result

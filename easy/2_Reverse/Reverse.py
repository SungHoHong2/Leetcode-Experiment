from typing import List, Dict

class Solution(object):
    def reverse(self, x: int) -> int:
        print(x)

        # check if the x is beyond the range of the integer
        # The most significant bit is used to code the sign (1 meaning negative),
        # so only 31 bits are available for the actual value.

        # 2^32 possible values
        # − 2^31 values used for negative integers
        # − 1 value used for zero
        # = 2^31−1 values available for positive integers

        # can't represent everything from −2^31 to 2^31 as that would be 2^32+1 numbers
        # So, we have to lop off one end.

        if x >= 2**31-1 or x <= -2**31:
            return 0

        reversed = ""
        strint = str(x)
        if x >= 0:
            reversed = strint[::-1]
        else:
            temp = strint[1:]
            reversed = "-" + temp[::-1]

        reversed = int(reversed)

        if reversed >= 2**31-1 or reversed <= -2**31:
            return 0
        else:
            # print(reversed)
            return reversed

def main():
    arg1 = 123
    return Solution().reverse(arg1)

if __name__ == "__main__":
    main()

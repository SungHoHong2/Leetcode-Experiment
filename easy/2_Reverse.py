from typing import List, Dict

class Solution(object):
    def reverse(self, x: int) -> int:
        print(x)

        if x >= 2**31-1 or x <= -2**31-1:
            return 0

        reversed = ""
        strint = str(x)
        if x >= 0:
            reversed = strint[::-1]
        else:
            temp = strint[1:]
            reversed = "-" + temp[::-1]

        reversed = int(reversed)

        if reversed >= 2**31-1 or reversed <= -2**31-1:
            return 0
        else:
            # print(reversed)
            return reversed

def main():
    arg1 = 123
    return Solution().reverse(arg1)

if __name__ == "__main__":
    main()

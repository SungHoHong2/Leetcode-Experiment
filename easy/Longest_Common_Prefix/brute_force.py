# Brute force
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        shortest_length = float("inf")

        rtnStr = ""

        if len(strs) == 0:
            shortest_length = 0

        for str in strs:
            if len(str) < shortest_length:
                shortest_length = len(str)

        for index in range(0, shortest_length):

            compare = None

            for str in strs:
                print(str[index])

                if compare is None:
                    compare = str[index]
                elif compare == str[index]:
                    compare = str[index]
                else:
                    return rtnStr

            rtnStr += compare

        return rtnStr




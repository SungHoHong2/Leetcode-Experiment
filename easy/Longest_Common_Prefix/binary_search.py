class Solution:

    def isCommonPrefix(self, strs: List[str], length: int) -> bool:

        str1 = strs[0][0:length]

        for i in range(1, len(strs)):
            if strs[i][0:length] != str1:
                return False
        return True

    def longestCommonPrefix(self, strs: List[str]) -> str:

        if strs is None or len(strs) == 0:
            return ""

        minLen = float("inf")

        for str in strs:
            if len(str) < minLen:
                minLen = len(str)

        low = 1
        high = int(minLen)

        # print('before', low, high)

        while low <= high:

            middle = int((low + high) / 2)
            if self.isCommonPrefix(strs, middle):
                low = middle + 1
            else:
                high = middle - 1
            # print('loop', low, high, middle)

        middle = int((low + high) / 2)
        # print('result', low, high, strs[0][0:middle])
        return strs[0][0:middle]





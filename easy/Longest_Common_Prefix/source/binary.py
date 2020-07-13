class Solution:

    def isCommonPrefix(self, strs: List[str], length: int) -> bool:

        # get substring for comparison
        str1 = strs[0][0:length]

        # compare the substring with all the given strings
        for i in range(1, len(strs)):
            if strs[i][0:length] != str1:
                return False

        return True

    def longestCommonPrefix(self, strs: List[str]) -> str:

        if strs is None or len(strs) == 0:
            return ""

        # get the shortest length of the given strings
        minLen = float("inf")
        for str in strs:
            if len(str) < minLen:
                minLen = len(str)

        # set up flags for the high and low of the binary tree
        low = 1
        high = int(minLen)

        # loop until the low and high converge
        while low <= high:

            # create the length of the substring
            middle = (low + high) // 2

            # if all the strings match with substring
            if self.isCommonPrefix(strs, middle):
                # increase the length of the substring
                low = middle + 1
            # if the strings does not match with substring
            else:
                # decrease the length of the substring
                high = middle - 1

        # return the final length of the substring
        middle = (low + high) // 2
        return strs[0][0:middle]

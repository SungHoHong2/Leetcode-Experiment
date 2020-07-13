class Solution:

    def divide(self, strs: List[str], left: int, right: int) -> str:

        # reached the end of the recursion (comparing the string itself)
        if left == right:
            return strs[left]

        # find the middle
        mid = int((left + right) / 2)

        # divide the strings and return the common substrings
        lcpLeft = self.divide(strs, left, mid)
        lcpRight = self.divide(strs, mid + 1, right)

        # get the shortest length of the common substrings from left and right
        min = 0
        if len(lcpLeft) < len(lcpRight):
            min = len(lcpLeft)
        else:
            min = len(lcpRight)

        # return the common substring
        for i in range(0, min):

            # if only the portion of the subtring from right and left are identical
            if lcpLeft[i] != lcpRight[i]:
                return lcpLeft[0:i]

        # if the whole substring from right and left are identical
        return lcpLeft[0:min]

    def longestCommonPrefix(self, strs: List[str]) -> str:

        # if the string has nothing return nothing
        if strs is None or len(strs) == 0:
            return ""

        # invoke recursive function (most left and right string)
        return self.divide(strs, 0, len(strs) - 1)






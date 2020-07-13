# Vertical Search
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # if there is no substring to compare
        if len(strs) == 0:
            return ""

        # get the length of shortest string
        shortLength = float('inf')
        for str in strs:
            if len(str) < shortLength:
                shortLength = len(str)

                # start a vertical comparison
        # check the substring only up to the shortest length
        rtnStr = ""
        for i in range(0, shortLength):

            compare = None
            # get all the equal substrings from all the strings
            for str in strs:
                # new character to compare
                if compare is None:
                    compare = str[i]

                    # if the character is equal
                elif compare == str[i]:
                    compare = str[i]

                    # if the substring ends
                else:
                    return rtnStr

                    # aggregate the common substring
            rtnStr += compare

        # return the common substring
        return rtnStr



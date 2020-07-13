#                                ----------------------------------
#                                input ['flower', 'flow', 'flight']
#                                ----------------------------------
#                                                 |
#                         -------------------------------------------------
#                         ['flower', 'flow', 'flight']  left = 0, right = 2
#                                                 |
#                                           return "flow"
#                         -------------------------------------------------
#                                  /                                  \
#                 --------------------------------     --------------------------------
#                 ['flower', 'flow', 'flight'] 0 1     ['flower', 'flow', 'flight'] 2 2
#                               |                                   |
#                           return "flow"                      return "flight"
#                 --------------------------------     --------------------------------
#                      /                      \
#   --------------------------------      --------------------------------
#   ['flower', 'flow', 'flight'] 0 0      ['flower', 'flow', 'flight'] 1 1
#                |                                        |
#          return 'flower'                          return "flow"
#   --------------------------------      --------------------------------

class Solution:
    counter = 0

    def divide(self, strs: List[str], left: int, right: int) -> str:

        print('recursive before', self.counter, strs, left, right)
        self.counter += 1

        if left == right:
            return strs[left]

        mid = int((left + right) / 2)

        lcpLeft = self.divide(strs, left, mid)
        lcpRight = self.divide(strs, mid + 1, right)

        print('recursive after', self.counter, strs, left, right, lcpLeft, lcpRight)
        self.counter += 1

        min = 0
        if len(lcpLeft) < len(lcpRight):
            min = len(lcpLeft)
        else:
            min = len(lcpRight)

        for i in range(0, min):
            if lcpLeft[i] != lcpRight[i]:
                return lcpLeft[0:i]

        return lcpLeft[0:min]

    def longestCommonPrefix(self, strs: List[str]) -> str:

        print('input', strs)

        # if the string has nothing return nothing
        if strs is None or len(strs) == 0:
            return ""

        return self.divide(strs, 0, len(strs) - 1)






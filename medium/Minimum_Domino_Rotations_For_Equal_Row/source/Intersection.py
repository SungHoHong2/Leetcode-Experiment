import functools
import operator

class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        # combine elements of A, B together as a set
        print([set(d) for d in zip(A, B)])
        # get the common value checking the combined sets
        s = functools.reduce(operator.and_, (set(d) for d in zip(A, B)))
        # if there is no common value
        if not s:
            # return false
            return -1
        # if there is a common value
        x = s.pop()
        # return the minimum number of swaps
        return min(len(A) - A.count(x), len(B) - B.count(x))
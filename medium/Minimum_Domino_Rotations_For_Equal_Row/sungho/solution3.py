import functools
import operator

class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        s = functools.reduce(operator.and_, (set(d) for d in zip(A, B)))

        if not s: return -1
        x = s.pop()
        return min(len(A) - A.count(x), len(B) - B.count(x))
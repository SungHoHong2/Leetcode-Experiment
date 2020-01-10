class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:

        # either the top or the bottom
        for cand in set([A[0], B[0]]):
            count_top = count_bottom = 0

            for i in range(len(A)):
                if cand not in (A[i], B[i]): break

                if cand != B[i]:
                    count_top += 1

                if cand != A[i]:
                    count_bottom += 1

            else:
                return min(count_top, count_bottom)

        return -1
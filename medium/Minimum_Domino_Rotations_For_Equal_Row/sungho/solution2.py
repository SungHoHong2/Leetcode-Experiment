class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        # Try make A[0] in a whole row,
        # the condition is that A[i] == A[0] || B[i] == A[0]
        # a and b are the number of swap to make a whole row A[0]

        # Try B[0]
        # the condition is that A[i] == B[0] || B[i] == B[0]
        # a and b are the number of swap to make a whole row B[0]

        # Return -1

        if len(A) != len(B): return -1
        if len(A) == 0: return 0

        for cand in set([A[0], B[0]]):  # Candidates.
            count_top = count_bottom = 0
            for i in range(len(A)):
                if cand not in (A[i], B[i]): break
                count_top += int(cand != B[i])
                count_bottom += int(cand != A[i])
            else:
                return min(count_top, count_bottom)

        return -1
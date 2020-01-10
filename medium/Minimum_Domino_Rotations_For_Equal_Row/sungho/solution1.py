class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:

        # A = [2,1,2,4,2,2]
        # B = [5,2,6,2,3,2]
        # countA[2] = 4, as A[0] = A[2] = A[4] = A[5] = 2
        # countB[2] = 3, as B[1] = B[3] = B[5] = 2
        # same[2] = 1, as A[5] = B[5] = 2
        # We have countA[2] + countB[2] - same[2] = 6
        # so we can make 2 in a whole row.

        countA = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}
        countB = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}
        same = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}

        n = len(A)

        for i in range(n):
            countA[A[i]] += 1
            countB[B[i]] += 1
            if A[i] == B[i]:
                same[A[i]] += 1

        for i in range(1, 7):
            if countA[i] + countB[i] - same[i] == n:
                return n - max(countA[i], countB[i])

        return -1





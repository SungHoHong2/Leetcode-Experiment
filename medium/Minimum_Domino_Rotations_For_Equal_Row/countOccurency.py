class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        c_a = [0] * 7
        c_b = [0] * 7
        same = [0] * 7
        for i in range(len(A)):
            c_a[A[i]] += 1
            c_b[B[i]] += 1
            if A[i] == B[i]:
                same[A[i]] += 1

        for i in range(1, 7):
            if c_a[i] + c_b[i] - same[i] == len(A):
                return len(A) - max(c_a[i], c_b[i])

        return -1

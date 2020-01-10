class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        r_a = 0
        r_b = 0
        result = 0
        for i in range(0, len(A)):
            if A[i] == A[0] or B[i] == A[0]:
                if A[i] != A[0]:
                    r_a += 1
                if B[i] != A[0]:
                    r_b += 1
                result = min(r_a, r_b)
            else:
                result = -1
                break

        if result != -1 or A[0] == B[0]:
            return result

        r_a = 0
        r_b = 0
        result = 0
        for i in range(0, len(B)):
            if A[i] == B[0] or B[i] == B[0]:
                if A[i] != B[0]:
                    r_a += 1
                if B[i] != B[0]:
                    r_b += 1
                result = min(r_a, r_b)
            else:
                result = -1
                break

        return result


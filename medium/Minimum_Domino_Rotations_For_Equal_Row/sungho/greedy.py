class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:

        def check(x, n):
            rot_a = rot_b = 0
            for i in range(0, n):
                if A[i] != x and B[i] != x:
                    return -1
                elif A[i] != x:
                    rot_a += 1
                elif B[i] != x:
                    rot_b += 1

            return min(rot_a, rot_b)

        n = len(A)
        rotation = check(A[0], n)
        # if it is -1 and also A and B are the same
        # the application can skip checking the B.
        if rotation != -1 or A[0] == B[0]:
            return rotation
        else:
            return check(B[0], n)

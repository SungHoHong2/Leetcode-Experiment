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

        # invoke the check function and get the minimum number of rotations
        rotation = check(A[0], len(A))
        # if the rotation value is valid or A and B have the same value
        if rotation != -1 or A[0] == B[0]:
            # return the minimun numvber of rotations
            return rotation
        # if the rotation does not provide any value
        else:
            # get the return value from B
            return check(B[0], len(B))

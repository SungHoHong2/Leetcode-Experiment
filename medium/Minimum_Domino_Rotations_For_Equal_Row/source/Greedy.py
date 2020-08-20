class Solution:
    def check(self, x, n):
        # set up the variable for rotations made by A and. B
        rot_a = rot_b = 0
        # iterate the dominos
        for i in range(0, n):
            # if both A and B are different from the target
            if A[i] != x and B[i] != x:
                # return false
                return -1
            # if A is wrong
            elif A[i] != x:
                # rotate A
                rot_a += 1
            # if B is wrong
            elif B[i] != x:
                # rotate B
                rot_b += 1
        # return the minimum number of rotations
        return min(rot_a, rot_b)
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        # invoke the check function and get the minimum number of rotations
        rotation = self.check(A[0], len(A))
        # if the rotation value is valid or A and B have the same value
        if rotation != -1 or A[0] == B[0]:
            # return the minimun numvber of rotations
            return rotation
        # if the rotation does not provide any value
        else:
            # get the return value from B
            return self.check(B[0], len(B))

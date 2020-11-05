class Solution:
    def check(self, A, B, x):
        # set up the variable for rotations made by A and. B
        rot_a = rot_b = 0
        # iterate the dominos
        for i in range(0, len(A)):
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
        rotation = self.check(A, B, A[0])

        # if the rotation value is valid or A and B have the same value
        if rotation != -1 or A[0] == B[0]:
            return rotation
        # if the rotation does not provide any value
        else:
            return self.check(A, B, B[0])


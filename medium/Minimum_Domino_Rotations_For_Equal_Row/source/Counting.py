class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        # create a map counting the number of hits for A
        countA = {i: 0 for i in range(7)}
        # create a map counting the number of hits for B
        countB = {i: 0 for i in range(7)}
        # create a map counting the number of hits for both A and B
        same = {i: 0 for i in range(7)}
        # iterate the dominos
        for i in range(len(A)):
            # count the number of hits for A
            countA[A[i]] += 1
            # count the number of hits for B
            countB[B[i]] += 1
            # if both A and B are equal
            if A[i] == B[i]:
                # count the number of hits for both A and B
                same[A[i]] += 1
        # iterate through the map
        for i in range(1, 7):
            # if the hits from A and B - (both) equals the total number of dominos
            if countA[i] + countB[i] - same[i] == len(A):
                # return the shortest possible result
                return len(A) - max(countA[i], countB[i])
        # if cannot find return false
        return -1


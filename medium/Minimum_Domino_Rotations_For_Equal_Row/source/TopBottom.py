class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        # iterate two candidate from A and B
        for cand in [A[0], B[0]]:
            # set the variable for counting the top and the bottom
            count_top = count_bottom = 0
            # iterate the dominos
            for i in range(len(A)):
                # if the candidate is not part of A or B then break
                if cand not in (A[i], B[i]): break
                # if candidate is not found in B
                if cand != B[i]:
                    # count the bottom
                    count_bottom += 1
                # if the candidate is not found in A
                if cand != A[i]:
                    # count the top
                    count_top += 1
            # if the no break after iterating the dominos
            else:
                # return the minimum number of rotations
                return min(count_top, count_bottom)
        # return the -1
        return -1
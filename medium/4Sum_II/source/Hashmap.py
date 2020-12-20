class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        # set a return variable that records the number possible solutions
        cnt = 0
        # create a table that records the complements
        m = collections.defaultdict(int)
        # iterate both list A and B
        for a in A:
            for b in B:
                # record the number of all possible sum
                m[a + b] += 1
        # iterate both list C and D
        for c in C:
            for d in D:
                # accumulate the number of possible sum that equals to zero
                cnt += m[-(c + d)]
        # return the possible numbers
        return cnt
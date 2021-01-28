class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        """
        x                       = x+(0+0)
        x + (x+1)               = 2x+(0+1)
        x + (x+1) + (x+2) ...   = 3x+(1+2) ...
        """
        # return 1 if the input is 1
        if N == 1:
            return 1
        # construct the formula: x+(0+0)=N, 2x+(0+1)=N, 3x+(1+2)=N, ...
        cnt, prev = 0, 0
        for curr in range(N):
            # create the (prev + curr) == (0+0),(0+1),(1+2) ...
            sub = prev + curr
            prev = sub
            # create the div*x == x, 2x, 3x, ...
            div = curr + 1
            Q, R = divmod(N - sub, div)
            # # return the answer when the formula exceeds N
            if not((N - sub) // div):
                return cnt
            # # count the number of consecutive numbers if formual equals to N
            if not((N - sub) % div):
                cnt += 1
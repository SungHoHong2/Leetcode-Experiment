class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        if N == 1: return 1
        cnt, prev = 0, 0
        # x + (x+1) + (x+2) + ...  = N
        for i in range(N):
            # x+(0+0)=N, 2x+(0+1)=N, 3x+(1+2)=N, ...
            sub = i + prev
            prev = sub
            # (x)=N, (2x)+1=N, (3x)+3=N
            div = i + 1
            # get the result from the division
            Q, R = divmod(N - sub, div)
            # return the total count if quotient becomes zero
            if not Q:
                return cnt
            # if N is fully divided count the possible numbers
            if not R:
                cnt += 1
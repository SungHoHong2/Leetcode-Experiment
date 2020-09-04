# f(0): ""
# f(1): "("f(0)")"
# f(2): "("f(0)")"f(1), "("f(1)")"
# f(3): "("f(0)")"f(2), "("f(1)")"f(1), "("f(2)")"
# So f(n) = "("f(0)")"f(n-1) , "("f(1)")"f(n-2) "("f(2)")"f(n-3) ... "("f(i)")"f(n-1-i) ... "(f(n-1)")"

class Solution(object):

    def generateParenthesis(self, N):
        if N == 0: return ['']
        ans = []

        for c in range(N):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(N - 1 - c):
                    ans.append('({}){}'.format(left, right))
        return ans

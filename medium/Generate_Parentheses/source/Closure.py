# f(0): ""
# f(1): "("f(0)")"
# f(2): "("f(0)")"f(1), "("f(1)")"
# f(3): "("f(0)")"f(2), "("f(1)")"f(1), "("f(2)")"
# So f(n) = "("f(0)")"f(n-1) , "("f(1)")"f(n-2) "("f(2)")"f(n-3) ... "("f(i)")"f(n-1-c) ... "(f(n-1)")"

class Solution(object):
    def generateParenthesis(self, N):
        if N == 0: return ['']
        rtnArray = []
        # iterate the available total number of parenthesis
        for c in range(N):
            # get the list of answers when the number of opening is "c"
            for left in self.generateParenthesis(c):
                # get the list of answers when the number of opening is N - c - 1
                for right in self.generateParenthesis(N - 1 - c):
                    # generate the answer and add to the returning list
                    rtnArray.append('({}){}'.format(left, right))
        # return the list of answers
        return rtnArray
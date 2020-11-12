class Solution:
    def __init__(self):
        self.cache = dict()

    def generateParenthesis(self, n: int) -> List[str]:

        # f(0) = ''
        # f(1) = (f(1))
        # f(2) = (f(0))f(1) (f(1))
        # f(3) = (f(0))f(2) (f(1))f(1) (f(2))

        if n == 0:
            return ['']

        if n in self.cache:
            return self.cache[n]

        rtnArray = list()
        for c in range(n):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(n - c - 1):
                    rtnArray.append('({}){}'.format(left, right))

        self.cache[n] = rtnArray
        return self.cache[n]

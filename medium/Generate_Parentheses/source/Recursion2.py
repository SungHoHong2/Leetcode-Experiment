class Solution:

    def generate(self, ans):
        if len(ans) == self.size:
            if self.valid(ans):
                self.rtnArray.append(ans)
        else:
            self.generate(ans + '(')
            self.generate(ans + ')')

    def valid(self, A):
        bal = 0
        for c in A:
            bal = bal + (1 if c == '(' else -1)
            if bal < 0:
                return False
        return bal == 0

    def generateParenthesis(self, n: int) -> List[str]:
        self.rtnArray = list()
        self.size = n * 2
        self.generate("")
        return self.rtnArray




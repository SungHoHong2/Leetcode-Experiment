class Solution:
    def generate(self, ans, left, right, ansSize, rtnArray):

        if len(ans) == ansSize:
            rtnArray.append("".join(ans))
            return

        if left < (ansSize // 2):
            ans.append('(')
            self.generate(ans, left + 1, right, ansSize, rtnArray)
            ans.pop()

        if right < left:
            ans.append(')')
            self.generate(ans, left, right + 1, ansSize, rtnArray)
            ans.pop()

    def valid(self, ans):
        bal = 0
        for c in ans:
            if c == '(':
                bal += 1
            else:
                bal -= 1
            if bal < 0:
                return False
        return bal == 0

    def generateParenthesis(self, n: int) -> List[str]:
        rtnArray = list()
        self.generate([], 0, 0, n * 2, rtnArray)
        return rtnArray

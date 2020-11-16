class Solution:
    def generate(self, ans, left, right):
        if len(ans) == self.size:
            if len(ans) == self.size:
                self.rtnArray.append(ans)
        else:
            if left < (self.size // 2):
                self.generate(ans + '(', left + 1, right)
            if right < left:
                self.generate(ans + ')', left, right + 1)

    def generateParenthesis(self, n: int) -> List[str]:
        self.rtnArray = list()
        self.size = n * 2
        self.generate("", 0, 0)
        return self.rtnArray
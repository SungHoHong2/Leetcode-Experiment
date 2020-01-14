class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return [""]
        result = []
        for i in xrange(n):
            for left in self.generateParenthesis(i):
                for right in self.generateParenthesis(n - i - 1):
                    result.append('({}){}'.format(left, right))

        return result
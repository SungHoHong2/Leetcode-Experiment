class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        def generate(A=[]):
            if len(A) == 2 * n:
                if valid(A):
                    result.append("".join(A))
            else:
                A.append("(")
                generate(A)
                A.pop()
                A.append(")")
                generate(A)
                A.pop()

        def valid(A):
            balance = 0
            for item in A:
                if item == "(":
                    balance += 1
                else:
                    balance -= 1

                if balance < 0:
                    return False
            return balance == 0

        result = []
        generate()
        return result

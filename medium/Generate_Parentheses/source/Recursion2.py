class Solution(object):
    def generate(self, ans):
        # set up the return array
        res = list()
        # if the generated answer has the expected length
        if len(ans) == self.size:
            # if the generated array contains
            if self.valid(ans):
                # add the answer to the return list
                res.append(ans)
        # if the generated answer does not have the expected length
        else:
            # invoke the recursive with additional opening
            res += self.generate(ans + '(')
            # invoke the recursive with additional closing
            res += self.generate(ans + ')')
        # return the parentheses
        return res

    def valid(self, ans):
        # set the balance to check the validity of the parenthesis
        bal = 0
        # iterate the list
        for c in ans:
            # if the list contains opening increment the balance
            if c == '(':
                bal += 1
                # if the list contains closing decrement the balance
            elif c == ')':
                bal -= 1
                # if the number of closing is more than the opening
            if bal < 0:
                return False
        # return true if the number of opening and closing are equal
        return bal == 0

    def generateParenthesis(self, n):
        # set the total size of the parenthesis
        self.size = n * 2
        # return the list of answers from the recursion
        return self.generate("")
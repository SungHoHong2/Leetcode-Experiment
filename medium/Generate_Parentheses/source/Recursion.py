class Solution(object):
    def generate(self, ans, ansSize, rtnArray):
        # if the generated answer has the expected length
        if len(ans) == ansSize:
            # if the generated array contains
            if self.valid(ans):
                # add the answer to the return list
                rtnArray.append("".join(ans))
        # if the generated answer does not have the expected length
        else:
            # append opening
            ans.append('(')
            # go to the right child of the recursive tree
            self.generate(ans, ansSize, rtnArray)
            # go back to the parent
            ans.pop()
            # append closing
            ans.append(')')
            # go to the left child of the recursive tree
            self.generate(ans, ansSize, rtnArray)
            # go back to the parent of the recursive tree
            ans.pop()
    def valid(self, A):
        # initiate a flag for checking the balance
        bal = 0
        # iterate the list
        for c in A:
            # if the list contains opening increment the balance
            if c == '(':
                bal += 1
            # if the list contains closing decrement the balance
            else:
                bal -= 1
            # if the number closing is more than the opening
            if bal < 0: return False
        # return true if the number of opening and closing are equal
        return bal == 0
    def generateParenthesis(self, n):
        # set up the return array
        rtnArray = list()
        # invoke the generate function
        self.generate([], 2 * n, rtnArray)
        # return the list of answers
        return rtnArray
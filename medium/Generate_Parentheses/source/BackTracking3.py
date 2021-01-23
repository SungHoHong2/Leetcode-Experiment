class Solution(object):
    def backtrack(self, ans, left, right):
        # set up the return array
        res = list()
        # if the answer has the expected length
        if len(ans) == self.size:
            # include the answer to the return array
            if len(ans) == self.size:
                res.append(ans)
        # if the length of the generated string is not enough
        else:
            # if the number of opening is not enough
            if left < (self.size // 2):
                # run the recursion with additional opening
                res += self.backtrack(ans + '(', left + 1, right)
            # if the number of closing is smaller than opening
            if right < left:
                # run the recursion with additional closing
                res += self.backtrack(ans + ')', left, right + 1)
        # return the parentheses
        return res

    def generateParenthesis(self, n):
        # set the total size of the valid parenthesis
        self.size = n * 2
        # run the recursion function
        return self.backtrack("", 0, 0)
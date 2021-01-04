class Solution(object):
    def generate(self, ans, left, right):
        # if the answer has the expected length
        if len(ans) == self.size:
            # include the answer to the return array
            if len(ans) == self.size:
                self.rtnArray.append(ans)
        # if the length of the generated string is not enough
        else:
            # if the number of opening is not enough
            if left < (self.size // 2):
                # run the recursion with additional opening
                self.generate(ans + '(', left + 1, right)
            # if the number of closing is smaller than opening
            if right < left:
                # run the recursion with additional closing
                self.generate(ans + ')', left, right + 1)

    def generateParenthesis(self, n):
        # set the return list
        self.rtnArray = list()
        # set the total size of the valid parenthesis
        self.size = n * 2
        # run the recursion function
        self.generate("", 0, 0)
        # return the list of answers
        return self.rtnArray
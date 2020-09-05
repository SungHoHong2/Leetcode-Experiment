class Solution(object):
    def backtrack(self, ans, left, right, ansSize, rtnArray):
        # if the answer has the expected length
        if len(ans) == ansSize:
            # include the answer to the return array
            rtnArray.append(ans)
            # finish the recursive function
            return
        # if the number of opnening is not enough
        if left < (ansSize // 2):
            # create an answer with additional opening
            self.backtrack(ans + '(', left + 1, right, ansSize, rtnArray)
        # if the number of closing is smaller than opening
        if right < left:
            # create an answer with additional closing
            self.backtrack(ans + ')', left, right + 1, ansSize, rtnArray)
    def generateParenthesis(self, N):
        # set the return list
        rtnArray = list()
        # run the backtrack function
        self.backtrack('',0,0, N*2, rtnArray)
        # return the list of answers
        return rtnArray
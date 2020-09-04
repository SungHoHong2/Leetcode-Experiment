class Solution(object):
    def generateParenthesis(self, N):
        # set the return list
        ans = list()
        def backtrack(S='', left=0, right=0):
            # if the length is twice as the original
            if len(S) == 2 * N:
                # include the answer to the return array
                ans.append(S)
                # finish the recursive function
                return
            # if more opening can be created
            if left < N:
                # create an answer with additional opening
                backtrack(S + '(', left + 1, right)
            # if the number of closing is smaller than opening
            if right < left:
                # create a answeir with additional closing
                backtrack(S + ')', left, right + 1)

        backtrack()
        return ans
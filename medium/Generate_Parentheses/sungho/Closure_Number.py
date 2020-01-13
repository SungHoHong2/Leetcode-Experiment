# Express it as a sum of disjoint subsets that are easier to count.
# For each closure number c, we know the starting and ending brackets must be at index 0 and 2*c + 1.
# Then, the 2*c elements between must be a valid sequence, plus the rest of the elements must be a valid sequence.

class Solution(object):
    def __init__(self):
        self.num = 0

    def generateParenthesis(self, N):
        if N == 0: return ['']
        ans = []

        for c in range(N):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(N - 1 - c):
                    ans.append('({}){}'.format(left, right))

        # print(N, ans)
        return ans

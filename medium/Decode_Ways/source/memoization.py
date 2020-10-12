class Solution:
    def __init__(self):
        # set a map to record the possible characters
        self.memo = {}

    def recursive_with_memo(self, index, s) -> int:
        # if the recursive tree reaches the largest index
        if index == len(s):
            return 1
        # If the string starts with a zero, it can't be decoded
        if s[index] == '0':
            return 0
        # if the recursive tree reaches the second largest index
        if index == len(s)-1 :
            return 1
        # return the recorded result if the same number is found
        if index in self.memo:
            return self.memo[index]
        # get the results from the recursive function using a single number and valid two digit number
        ans = self.recursive_with_memo(index+1, s) + (self.recursive_with_memo(index+2, s) if (int(s[index : index+2]) <= 26) else 0)
        # record the result for the current number
        self.memo[index] = ans
        # return the result
        return self.memo[index]

    def numDecodings(self, s: str) -> int:
        # if there is no input
        if not s:
            # return 0
            return 0
        # invoke the recursive tree
        return self.recursive_with_memo(0, s)
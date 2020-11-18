class Solution:
    def __init__(self):
        self.index = 0
    def decodeString(self, s: str) -> str:
        # set the result string
        currString = ''
        # iterate until the input is depleted to the end
        while self.index < len(s) and s[self.index] != ']':
            # if the string is not a digit
            if not s[self.index].isdigit():
                # append to the result
                currString += s[self.index]
                # increase the index
                self.index += 1
            # if the string is a digit
            else:
                # get the total number of integers
                repeat = 0
                while self.index < len(s) and s[self.index].isdigit():
                    repeat = repeat * 10 + int(s[self.index])
                    self.index += 1
                # ignore the open bracket
                self.index += 1
                # invoke the recursive
                prevString = self.decodeString(s)
                # ignore the closing bracket
                self.index += 1
                # add the repeated number of strings from the recursive function
                currString += prevString * repeat
        # return the result
        return currString




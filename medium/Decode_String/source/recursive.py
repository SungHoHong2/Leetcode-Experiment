class Solution:
    def __init__(self):
        # set the global index
        self.index = 0

    def decodeString(self, s: str) -> str:
        # set the result string
        currString = ''
        # iterate until the input is depleted to the end
        while self.index < len(s) and s[self.index] != ']':
            # if the string is a digit
            if s[self.index].isdigit():
                # compute the repeats
                repeat = 0
                while self.index < len(s) and s[self.index].isdigit():
                    repeat = repeat * 10 + int(s[self.index])
                    self.index += 1
                # ignore the open bracket
                self.index += 1
                # get the string from recursive operations
                prevString = self.decodeString(s)
                # ignore the closing bracket
                self.index += 1
                # add the repeated number of strings from the recursive function
                currString += prevString * repeat
            # if the string is not a digit
            else:
                # append to the result
                currString += s[self.index]
                # increase the index
                self.index += 1
        # return the result
        return currString
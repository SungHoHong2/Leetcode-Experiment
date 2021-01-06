class Solution:
    def __init__(self):
        # set the global index
        self.index = 0

    def decodeString(self, s: str) -> str:
        # set the result string
        currString = ''
        # iterate until the input is depleted to the end or the current index is not a char
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
                # add the repeated number of strings from the recursive function
                currString += self.decodeString(s) * repeat
                # ignore the closing bracket
                self.index += 1
            # if the string is not a digit
            else:
                # append to the result
                currString += s[self.index]
                # increase the index
                self.index += 1
        # return the result
        return currString
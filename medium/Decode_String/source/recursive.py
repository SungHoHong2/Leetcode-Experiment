class Solution:
    """
    using internal stack
        replace the stack with the internal stack
        3[a]2[bc] = [a] [bc] are constructed by recursion
    """
    def __init__(self):
        # set the global index
        self.index = 0
    def decodeString(self, s: str) -> str:
        # set the result string
        curr = ''
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
                # accumulate the strings from recursive operations
                curr += self.decodeString(s) * repeat
                # ignore the closing bracket
                self.index += 1
            # if the string is not a digit
            else:
                # append to the result
                curr += s[self.index]
                # increase the index
                self.index += 1
        # return the result
        return curr
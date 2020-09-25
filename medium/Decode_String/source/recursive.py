class Solution:
    # set the global index
    index = 0
    def decodeString(self, s: str) -> str:
        # set the result string
        result = ''
        # iterate until the input is depleted to the end
        while self.index < len(s) and s[self.index] != ']':
            # if the string is not a digit
            if not s[self.index].isdigit():
                # append to the result
                result += s[self.index]
                # increase the index
                self.index += 1
            # if the string is a digit
            else:
                # get the total number of integers
                k = 0
                while self.index < len(s) and s[self.index].isdigit():
                    k = k * 10 + int(s[self.index])
                    self.index += 1
                # ignore the open bracket
                self.index += 1
                # invoke the recursive
                decodeStr = self.decodeString(s)
                # ignore the closing bracket
                self.index += 1
                # add the repeated number of strings from the recursive function
                while k > 0:
                    k -= 1
                    result += decodeStr
        # return the result
        return result




class Solution:
    def decodeString(self, s: str) -> str:
        # set the stack
        stack = list()
        # set the repeat
        repeat = 0
        # set the current string
        currString = ""
        # iterate the input
        for c in s:
            # if the input is a digit
            if c.isdigit():
                # set the repeat
                repeat = repeat * 10 + int(c)
            # if the char is open
            elif c == '[':
                # save the repeat
                stack.append(repeat)
                # save the current string as the previous string
                stack.append(currString)
                # renew the repeat and the current string
                repeat = 0
                currString = ""
            # if the char is close
            elif c == ']':
                # restore the previous string and repeat
                currString = str(stack.pop()) + currString * int(stack.pop())
                # attach the previous with the newly formed string
            # if the char is an alphabet
            else:
                # append it to the current string
                currString += c
        # return the result
        return currString

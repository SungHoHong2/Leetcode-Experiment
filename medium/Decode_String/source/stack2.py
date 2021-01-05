class Solution:
    def decodeString(self, s: str) -> str:
        # create a stack that stores the current string and the repeated number
        stack = list()
        # initialize the pointer of repeat and current string
        repeat, currString = 0, ""
        # iterate the input
        for c in s:
            # if char is part of the repeat number
            if c.isdigit():
                # record the repeat considering the number may be two digits (ex 32[a])
                repeat = repeat * 10 + int(c)
            # if the char is an opening bracket
            elif c == '[':
                # save the state of the number of repeats for the current string
                stack.append(repeat)
                # save the state of the previously created string
                stack.append(currString)
                # renew the state of the repeat and the current string
                repeat, currString = 0, ""
            # if the char is a closing bracket
            elif c == ']':
                # combine the previous result with the repeating current string
                currString = str(stack.pop()) + int(stack.pop()) * currString
            # if char is a data
            else:
                # append the char to the current string
                currString += c
        # return the accumulated result
        return currString
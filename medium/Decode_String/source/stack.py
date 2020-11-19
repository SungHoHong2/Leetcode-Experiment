class Solution:
    def decodeString(self, s: str) -> str:
        # create a stack that stores the current string and the repeated number
        stack = list()
        # intialize the pointer of current string
        currString = ""
        # initizlie the pointer of repeated numbers
        repeat = 0
        # iterate the input
        for c in s:
            # if char is the repeat number
            if c.isdigit():
                # if the repeat is two digits (ex 32[a])
                repeat = repeat * 10 + int(c)
            # if it is a opening bracket
            elif c == '[':
                # save the state of the previous string
                stack.append(currString)
                # save the state for the number of repeats for the current string
                stack.append(repeat)
                # set the current string pointer to zero
                currString = ""
                # set the repeat pointer to zero
                repeat = 0
            # if it is a closing bracket
            elif c == ']':
                # pop out the number from the stack
                number = stack.pop()
                # pop out the previous string from the stack
                prevString = stack.pop()
                # append the string with the new repeated data
                currString = prevString + currString * number
            # if char is a data
            else:
                # append the char
                currString += c
        # return the accumulated result
        return currString
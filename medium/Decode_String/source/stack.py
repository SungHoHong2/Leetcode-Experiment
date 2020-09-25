class Solution:
    def decodeString(self, s: str) -> str:
        # create a stack that stores the current string and the repeated number
        stack = []
        # intialize the pointer of current string
        curString = ''
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
                # first add the currently accumulated string
                stack.append(curString)
                # add the number of repeats
                stack.append(repeat)
                # set the current string pointer to zero
                curString = ''
                # set the repeat pointer to zero
                repeat = 0
                # if it is a closing bracket
            elif c == ']':
                # pop out the number from the stack
                num = stack.pop()
                # pop out the current string from the stack
                prevString = stack.pop()
                # append the string with the new repeated data
                curString = prevString + num * curString
                # if char is a data
            else:
                # append the char
                curString += c
                # return the accumulated result
        return curString


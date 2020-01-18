class Solution:
    def decodeString(self, s: str) -> str:
        # Given an encoded string, return its decoded string.
        stack = []
        curNum = 0
        curString = ''

        for c in s:

            if c == '[':
                # put the <previous string (aggregating result)> in to the stack
                # put the <number of the current string> that needs to be repeated
                stack.append(curString)
                stack.append(curNum)
                curString = ''
                curNum = 0

            elif c == ']':
                num = stack.pop()
                prevString = stack.pop()

                # multiply the current string and add it tothe previous string
                curString = prevString + num * curString

            # if the digit is more than 10
            elif c.isdigit():
                # ex) 101[leetcode]
                curNum = curNum * 10 + int(c)

            # if the string is more than one character
            else:
                curString += c

        return curString


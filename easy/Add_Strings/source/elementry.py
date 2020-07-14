class Solution:
    def addStrings(self, num1: str, num2: str) -> str:

        # set up the return value
        res = []
        # set up the carry
        carry = 0
        # set up the strings into stack of numbers
        stack1 = [int(n) for n in num1]
        stack2 = [int(n) for n in num2]
        # until either num1 or num2 is depleted
        while stack1 or stack2:
            x1 = stack1.pop() if stack1 else 0
            x2 = stack2.pop() if stack2 else 0
            value = (x1 + x2 + carry) % 10
            # calculate the carry
            carry = (x1 + x2 + carry) // 10
            # append the result
            res.append(value)

        # if there is a carry left
        if carry:
            res.append(carry)

        # return the result as a string
        return ''.join(str(x) for x in res[::-1])
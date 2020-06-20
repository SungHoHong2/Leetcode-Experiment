class Solution:
    def addBinary(self, a: str, b: str) -> str:

        # initialize the answer stack
        rtnStack = []

        # initialize the carry
        carry = 0

        # a stack of "a" and "b"
        stackA = [int(i) for i in a]
        stackB = [int(i) for i in b]
        # print(arrayA, arrayB)

        # iterate the strings "a" and "b" until one of them are depleted
        while stackA or stackB:

            # calculation sum = a + b + carry
            sum = 0

            if stackA:
                sum += stackA.pop()

            if stackB:
                sum += stackB.pop()

            sum += carry

            ans = sum % 2
            carry = sum // 2

            rtnStack.append(ans)
            # print(sum, ans, carry)

        if carry:
            rtnStack.append(carry)

        return "".join(str(i) for i in rtnStack[::-1])










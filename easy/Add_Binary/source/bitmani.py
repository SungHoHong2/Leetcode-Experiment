class Solution:
    def addBinary(self, a, b) -> str:
        # convert the string into bit
        x, y = int(a, 2), int(b, 2)

        # either choose x as a carry and y as an answer or y as a carry and x as an answer

        # iterate until there is no more to carry
        while x:
            # use the XOR to generate the answer
            answer = x ^ y

            # use AND and move to left to generate the carry
            carry = (x & y) << 1

            # assign the answer to X and the carry to Y for the next iteration
            y, x = answer, carry
            # print(bin(x),bin(y))

        return bin(y)[2:]
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:

        res = ""

        # if the result of the division is negative
        if numerator / denominator < 0:
            res += "-"

        # if the result of the division clearly divides
        if numerator % denominator == 0:
            return str(numerator // denominator)


        numerator = abs(numerator)
        denominator = abs(denominator)

        # add the upper number and the dot to the result
        # ex) 0.
        res += str(numerator // denominator)
        res += "."


        # get the remainder
        numerator %= denominator
        i = len(res)

        table = {}

        # run the loop until numerator becomes zero
        while numerator != 0:

            # if the current remainder is not in the table
            if numerator not in table.keys():
                # add the remainder in the table with the index of the number
                table[numerator] = i

            # if the current remainder is found in the table
            else:
                # get the index
                i = table[numerator]

                # use it to wrap the repeated remainders
                res = res[:i] + "(" + res[i:] + ")"
                return res

            # multiply the remainder with 10
            numerator = numerator * 10

            # add the remainder to the result
            res += str(numerator // denominator)

            # divide the remainder
            numerator %= denominator

            # increase the index
            i += 1
        return res

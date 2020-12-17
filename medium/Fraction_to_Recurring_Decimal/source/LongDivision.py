class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # set the return string
        res = ""
        # add "-" to the return if the result of the division is negative
        if numerator / denominator < 0:
            res += "-"
        # return the result directly if the result has no remainder
        if numerator % denominator == 0:
            return str(numerator // denominator)
        # set the numerator and denominator to absolute
        numerator = abs(numerator)
        denominator = abs(denominator)
        # append the divided result
        res += str(numerator // denominator)
        # append the dot
        res += '.'
        # get the remainder
        remainder = numerator % denominator
        # get the starting position of the remainder
        i = len(res)
        # set a map to track the repeating remainder
        table = dict()
        # run the loop until the remainder becomes zero
        while remainder != 0:
            # if the current remainder is not in the table
            if remainder not in table:
                # add the remainder in the table with the index of the string
                table[remainder] = i
            # if the current remainder is found in the table
            else:
                # get the staring position of the repeating number
                i = table[remainder]
                # return the result wrapped the repeated remainders
                return res[:i] + "(" + res[i:] + ")"
            # multiply the remainder with 10
            remainder = remainder * 10
            # add the divided result to the return string
            res += str(remainder // denominator)
            # get the next remainder
            remainder %= denominator
            # increase the index
            i += 1
        # return the string
        return res
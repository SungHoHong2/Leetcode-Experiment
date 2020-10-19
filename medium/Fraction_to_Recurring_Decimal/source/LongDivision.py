class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # set the return string
        res = ""
        # add "-" to the return if the result of the division is negative
        if numerator / denominator < 0:
            res += "-"
        # return the result directly if the result of the division divides without the remainder
        if numerator % denominator == 0:
            return str(numerator // denominator)
        # set the numerator and denominator as absolute
        numerator = abs(numerator)
        denominator = abs(denominator)
        # append the divided result
        res += str(numerator // denominator)
        # append the dot
        res += "."
        # get the remainder
        numerator %= denominator
        # get the current length of the string
        i = len(res)
        # set a map to track the repeated results
        table = {}
        # run the loop until numerator becomes zero
        while numerator != 0:
            # if the current remainder is not in the table
            if numerator not in table.keys():
                # add the remainder in the table with the index of the string
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
            # add the divided result to the return string
            res += str(numerator // denominator)
            # get the next remainder
            numerator %= denominator
            # increase the index
            i += 1
        # return the string
        return res
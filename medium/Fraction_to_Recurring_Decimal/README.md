### Fraction to Recurring Decimal
**Long Division**
- [Source code](source/LongDivision.py)
```python
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # set the return string 
        # add "-" to the return if the result of the division is negative
        # return the result directly if the result has no remainder
        # set the numerator and denominator to absolute
        # append the divided result 
        # append the dot
        # get the remainder
        # get the starting position of the remainder
        # set a map to track the repeating remainder 
        # run the loop until the remainder becomes zero
            # if the current remainder is not in the table
                # add the remainder in the table with the index of the string 
            # if the current remainder is found in the table
                # get the staring position of the repeating number 
                # return the result wrapped the repeated remainders
            # multiply the remainder with 10
            # add the divided result to the return string 
            # get the next remainder
            # increase the index
        # return the string
        pass
```



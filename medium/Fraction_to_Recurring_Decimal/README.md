### Problem Title
**Long Division**
- [Source code](source/LongDivision.py)
```python
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # set the return string 
        # add "-" to the return if the result of the division is negative
        # return the result directly if the result of the division divides without the remainder
        # set the numerator and denominator as absolute
        # append the divided result 
        # append the dot
        # get the remainder
        # get the current length of the string 
        # set a map to track the repeated results 
        # run the loop until numerator becomes zero
            # if the current remainder is not in the table
                # add the remainder in the table with the index of the string 
            # if the current remainder is found in the table
                # get the index
                # use it to wrap the repeated remainders
            # multiply the remainder with 10
            # add the divided result to the return string 
            # get the next remainder
            # increase the index
        # return the string
        pass 
```



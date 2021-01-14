### UTF-8 Validation
**String Manipulation**
- [Source code](source/StringManipulate.py)
```python
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        # set the variable to keep track of the number of following bytes
        # iterate the numbers from the input
            # convert the numbers into binary representation of 8 bits
            # if the current byte is the first byte
                # count the total number of following bytes
                # continue if the there are no following bytes
                # return false if the first byte is a following byte or has more than 4 following bytes
            # if the current byte is a following byte
                # return false if the following byte is not a following byte
            # decrement the total number of following bytes
        # return true if all the bytes follow the rules
        pass
```

**Bit Manipulation**
- [Source code](source/BitManipulation.py)
```python
class Solution:
    def validUtf8(self, data):
        # set the variable to keep track of the number of following bytes
        # iterate the numbers from the input
            # set a mask = 10000000
            # if the current byte is the first byte
                # loop until the AND result becomes zero
                    # increase the number of total following bytes
                    # shift the mask to right 
                # continue if the there are no following bytes
                # return false if the first byte is a following byte or has more than 4 following bytes
            # if the current byte is a following byte
                # return false if the following byte is not a following byte
            # decrement the total number of following bytes
        # return true if all the bytes follow the rules
        pass
```
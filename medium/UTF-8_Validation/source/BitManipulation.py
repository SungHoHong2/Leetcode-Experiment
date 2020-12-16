class Solution:
    def validUtf8(self, data):
        # set the variable to keep track of the number of following bytes
        n_bytes = 0
        # set a mask by shifting 00000001 to left 7 times -> 10000000
        mask1 = 1 << 7
        # set a mask by shifting 00000001 to left 6 times -> 01000000
        mask2 = 1 << 6
        # iterate the numbers from the input
        for num in data:
            # set a mask by shifting 00000001 to left 7 times -> 10000000
            mask = 1 << 7
            # if the current byte is the first byte
            if n_bytes == 0:
                # loop until the AND result becomes zero
                while mask & num:
                    # increase the number of total following bytes
                    n_bytes += 1
                    # shift the mask to right
                    mask = mask >> 1
                # continue if the there are no following bytes
                if n_bytes == 0:
                    continue
                # return false if the first byte is a following byte or has more than 4 following bytes
                if n_bytes == 1 or n_bytes > 4:
                    return False
            # if the current byte is a following byte
            else:
                # return false if the following byte is not a following byte
                if not (num & mask1 and not(num & mask2)):
                    return False
            # decrement the total number of following bytes
            n_bytes -= 1
        # return true if all the bytes follow the rules
        return n_bytes == 0
class Solution:
    def validUtf8(self, data):
        # set the variable to keep track of the number of following bytes
        following_bytes = 0
        # iterate the numbers from the input
        for num in data:
            # set a mask by shifting 00000001 to left 7 times -> 10000000
            mask = 1 << 7
            # if the current byte is the first byte
            if following_bytes == 0:
                # loop until the AND result becomes zero
                while mask & num != 0:
                    # increase the number of total following bytes
                    following_bytes += 1
                    # shift the mask to right
                    mask = mask >> 1
                # continue if the there are no following bytes
                if following_bytes == 0 :
                    continue
                # return false if the first byte is a following byte or has more than 4 following bytes
                if following_bytes == 1 or following_bytes > 4:
                    return False
            # if the current byte is a following byte
            else:
                # return false if the following byte is not a following byte
                if not(num & (1 << 7) and not(num & (1 << 6))):
                    return False
            # decrement the total number of following bytes
            following_bytes -= 1
        # return true if all the bytes follow the rules
        return following_bytes == 0
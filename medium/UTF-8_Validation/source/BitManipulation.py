class Solution:
    def validUtf8(self, data):
        # set the variable to count the total number of grouped bytes
        n_bytes = 0
        # set the mask to check the most significant bit
        mask1 = 1 << 7
        # set the mask to check the second most significant bit
        mask2 = 1 << 6
        # iterate the numbers from the input
        for num in data:
            # set a mask to check the most significant bit
            mask = 1 << 7
            # if the number is the first byte of the group
            if n_bytes == 0:
                # loop until the num is not zero
                while mask & num:
                    # increase the number of total following bytes
                    n_bytes += 1
                    # shift the mask to mask the second significant bit
                    mask = mask >> 1
                # continue the loop if the there is only one byte in the group
                if n_bytes == 0:
                    continue
                # return false if there is only 1 or more than 4 at the first byte
                if n_bytes == 1 or n_bytes > 4:
                    return False
            # if the group is more than 1 and the first byte is valid
            else:
                # return false if the most significants 2bits are not 1,0
                if not (num & mask1 and not (num & mask2)):
                    return False
            # decrement the total number of bytes of the group
            n_bytes -= 1
        # return true if all the bytes in the group are processed
        return n_bytes == 0
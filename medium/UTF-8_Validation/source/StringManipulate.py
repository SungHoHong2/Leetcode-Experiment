class Solution:
    def validUtf8(self, data):
        # set the variable to count the total number of grouped bytes
        n_bytes = 0
        # iterate the numbers from the input
        for num in data:
            # convert the numbers into binary representation of 8 bits
            bin_rep = format(num, '#010b')[-8:]
            # if it is the first byte of the group
            if n_bytes == 0:
                # count the total number of following bytes until zero
                for bit in bin_rep:
                    if bit == '0': break
                    n_bytes += 1
                # continue the loop if the there is only one byte in the group
                if n_bytes == 0:
                    continue
                # return false if there is only 1 or more than 4 at the first byte
                if n_bytes == 1 or n_bytes > 4:
                    return False
            # if the group is more than 1 and the first byte is valid
            else:
                # return false if the most significants 2bits are not 1,0
                if not (bin_rep[0] == '1' and bin_rep[1] == '0'):
                    return False
            # decrement the total number of bytes of the group
            n_bytes -= 1
        # return true if all the bytes in the group are processed
        return n_bytes == 0
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        # set the variable to keep track of the number of following bytes
        n_bytes = 0
        # iterate the numbers from the input
        for num in data:
            # convert the numbers into binary representation of 8 bits
            bin_rep = format(num, '#010b')[-8:]
            # if the current byte is the first byte
            if n_bytes == 0:
                # count the total number of following bytes
                for bit in bin_rep:
                    if bit == '0': break
                    n_bytes += 1
                # continue if the there are no following bytes
                if n_bytes == 0:
                    continue
                # return false if the first byte is a following byte or has more than 4 following bytes
                if n_bytes == 1 or n_bytes > 4:
                    return False
            # if the current byte is a following byte
            else:
                # return false if the following byte is not a following byte
                if not (bin_rep[0] == '1' and bin_rep[1] == '0'):
                    return False
            # decrement the total number of following bytes
            n_bytes -= 1
        # return true if all the bytes follow the rules
        return n_bytes == 0
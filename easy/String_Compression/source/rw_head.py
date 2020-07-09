class Solution(object):
    def compress(self, chars):
        # anchor is used for counting the total repeated characters
        anchor = 0
        # write is used for writing the number of repeated characters in the array
        write = 0
        # iterate the character array
        for read, c in enumerate(chars):
            # if finished counting the repeated characters
            if read + 1 == len(chars) or chars[read + 1] != c:
                # place the start of the repeated character
                chars[write] = chars[anchor]
                write += 1
                # if there are more than one repeated characters
                if read > anchor:
                    # create a string of the repeated number
                    for digit in str(read - anchor + 1):
                        chars[write] = digit
                        write += 1
                # update the new start
                anchor = read + 1
        # the return limits the total number of characters evaluated
        return write
class Solution:
    def fullJustify(self, words, maxWidth):
        # set the return list, list of words, and the total length of words in the current line
        res, line, line_length = list(), list(), 0
        # iterate the words
        for w in words:
            # get the number of potential white spaces
            new_spaces = len(line)
            # get the length of the new word
            word_length = len(w)
            # if adding a new word with *extra one* more white spaces exceeds the maxWidth
            if new_spaces + word_length + line_length > maxWidth:
                # iterate up the empty spaces in the line
                for i in range(maxWidth - line_length):
                    # push the white spaces to the right if the line has a single word
                    if len(line)-1 == 0:
                        line[0] += ' '
                    # distribute the white spaces in RR if there are multiple word in the line
                    else:
                        line[i % (len(line)-1)] += ' '
                # append the result to the return array
                res.append(''.join(line))
                # reset the list of words and total number of chars in each line
                line, line_length = list(), 0
            # append the word for the current line
            line.append(w)
            # increase the length of the characters in the current line
            line_length += len(w)
        # create a left-aligned sentence for the last line
        for i in range(maxWidth - line_length):
            # distribute the white spaces in RR once
            if i < len(line) - 1:
                line[i % (len(line) - 1)] += ' '
            # after that push all the other white spaces to the right
            else:
                line[len(line) - 1] += ' '
        res.append(''.join(line))
        # return the result
        return res

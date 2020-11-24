class Solution:
    def fullJustify(self, words, maxWidth):
        # set the return list, list of words, and the total length of words in the current line
        res, cur, num_of_letters = [], [], 0
        # iterate the words
        for w in words:
            # the exceed the maxWidth
            if num_of_letters + len(w) + len(cur) > maxWidth:
                # subtract the maxWidth from the number of letters
                for i in range(maxWidth - num_of_letters):
                    # increase the number of blanks to each word in round robin
                    cur[0 if len(cur) - 1 == 0 else i % (len(cur) - 1)] += ' '
                    # append the result to the return array
                res.append(''.join(cur))
                # reset the list of words and total number of chars in each line
                cur, num_of_letters = [], 0
            # append the word for the current line
            cur.append(w)
            # increase the length of the characters in the current line
            num_of_letters += len(w)

        # create a left-aligned sentece for the last line
        for i in range(maxWidth - num_of_letters):
            if i < len(cur) - 1:
                cur[0 if len(cur) - 1 == 0 else i % (len(cur) - 1)] += ' '
            else:
                cur[len(cur) - 1] += ' '
        res.append(''.join(cur))

        # return the result
        return res
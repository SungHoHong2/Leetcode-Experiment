### Text Justification
**Round Robin**
- Concepts
    - Use round robin to add blanks for each words in each line
- [Source code](source/Solution.py)
```python
class Solution:
    def fullJustify(self, words, maxWidth):
        # set the return list, list of words, and the total length of words in the current line
        # iterate the words
            # get the one extra (end of the sentence) number of white spaces 
            # get the length of the new word
            # if adding a new word with *extra one* more white spaces exceeds the maxWidth  
                # iterate up the empty spaces in the line 
                    # push the white spaces to the right if the line has a single word 
                    # distribute the white spaces in RR if there are multiple word in the line
                # append the sentence to the return array
                # reset the list of words and total number of chars in each line
            # append the word for the current line
            # increase the length of the characters in the current line
        # create a left-aligned sentence for the last line
            # distribute the white spaces in RR once 
            # after that push all the other white spaces to the right
        # append the sentence to the return array
        # return the justified paragraph
        pass
```
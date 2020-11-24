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
            # the exceed the maxWidth
                # subtract the maxWidth from the number of letters
                    # increase the number of blanks to each word in round robin
                    # append the result to the return array
                # reset the list of words and total number of chars in each line
            # append the word for the current line
            # increase the length of the characters in the current line

        # create a left-aligned sentece for the last line
        # return the result
        pass
```
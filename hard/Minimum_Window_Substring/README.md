### Minimum Window Substring
**Sliding Window**
- [Source code](source/SlidingWindow.py)
```python
class Solution:
    def minWindow(self, s, t):
        # return empty string if the input is invalid
        # declare a hashmap that counts the frequency of the unqiue characters of string "t" 
        # get the total number of unique characters of string "t"
        # left and right pointer
        # keep track of number of characters of string "t" that are matched with string "s"
        # declare a hashmap that counts the frequency of the unqiue characters of the current window 
        # declare a tuple of the form (window length, left, right)
        # start expanding the window from the right
            # Add one character from the right to the window
            # add to the map  
            # check if the frequency of the character in the window matchs with the string "t"
            # start shrinking the window from the left once it contains the substring of "t" 
                # record the smallest window 
                # deduct the characters from the left index 
                # once the window does not satisfy the complete subset of string "t"
                    # reduce the number of matched frequency
                # shrink the window size 
            # increase the window size
        # return empty string if there is no match or return the matched substring
        pass
```

**Optimized Sliding Window**
- [Concepts](images/)
    - Consider a scenario:
        - length of string `t` is way too small than the length of string `s` 
        - string `s` consists of numerous characters which are not present in `t`
    - Store the index of the characters in `s` that matches with `t`
- [Source code](source/SlidingWindowOpt.py)
```python
class Solution:
    def minWindow(self, s, t):
        # return empty string if there is a invalid input
        # declare a hashmap that counts the frequency of the unqiue characters of string "t"
        # get the total number of unique characters of string "t"
        # filter all the characters from "s" into a new list along with their index.
        # left and right pointer
        # keep track of number of characters of string "t" that are matched with string "s"
        # declare a hashmap that counts the frequency of the unqiue characters of the current window
        # declare a tuple of the form (window length, left, right)
        # explore for the characters only in the filtered list instead of entire "s"
            # get one character from the right to the window
            # count the frequency of the characters in the window
            # check if the frequency of the character in the window matches with the string "t"
            # start recording the answer once the window contains the substring of "t"
                # record the smallest window
                # deduct the characters from the left index
                # once the window does not satisfy the complete subset of string "t"
                    # reduce the number of matched frequency
                # shrink the window size
            # increase the window size
        # return empty string if there is no match or return the matched substring
        pass
```

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

**Solution2**
- [Concepts](images/)
- [Source code](source/)
- [Reference #1]()

**Solution3**
- [Concepts](images/)
- [Source code](source/)
- [Reference #1]()
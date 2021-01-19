### Minimum Window Substring
**Sliding Window**
- [Source code](source/SlidingWindow.py)
```python
class Window:
    def __init__(self, length, left, right):
        self.length = length 
        self.left = left 
        self.right = right

class Solution:
    def minWindow(self, s, t):
        # return empty string if the input is invalid
        # set a hashmap that counts the frequency of the unique characters of the target     
        # keep track of number of characters of target that are matched with input
        # set a hashmap that counts the frequency of the unique characters of the current window 
        # set a returning tuple (window length, left, right)
        # set the left and right pointer
        # start expanding the window from the right
            # get the new character from the right 
            # add to the map  
            # check if the frequency of the character in the window matches with the target
            # start shrinking the window from the left once it contains the substring of the target 
                # get the old character from the left 
                # record the smallest window 
                # deduct the characters from the left index 
                # once the window does not satisfy the complete subset of the target
                    # reduce the number of matched frequency
                # shrink the window size 
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
class Filter:
    def __init__(self, index, char):
        self.index = index
        self.char = char

class Window:
    def __init__(self, length, left, right):
        self.length = length
        self.left = left
        self.right = right

class Solution:
    def minWindow(self, s, t):
        # return empty string if the input is invalid
        # set a hashmap that counts the frequency of the unique characters of the target
        # get the total number of unique characters of the target
        # filter all the characters from "s" into a new list along with their index.
        # left and right pointer
        # keep track of number of characters of target that are matched with input
        # set a hashmap that counts the frequency of the unique characters of the current window
        # set a returning tuple (window length, left, right)
        # start expanding the window from the right
            # get the new character from the right
            # add to the map
            # check if the frequency of the character in the window matches with the target
            # start shrinking the window from the left once it contains the substring of the target
                # get the old character from the left
                # record the smallest window
                # deduct the characters from the left index
                # once the window does not satisfy the complete subset of the target
                    # reduce the number of matched frequency
                # shrink the window size
        # return empty string if there is no match or return the matched substring
        pass
```

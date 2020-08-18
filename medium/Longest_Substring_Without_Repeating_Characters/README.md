### Longest Substring Without Repeating Characters
**Brute Force**
- [Source code](source/Brute.py)
```python
class Solution:
    def allUnique(self, s, start, end):
        # setup a hashset
        # iterate from start
            # if duplicate is found
                # return false
            # record the characters in the hashmap
        # return true if there is no duplicate found
    def lengthOfLongestSubstring(self, s: str) -> int:
        # set the return value 
        # iterate the entire string twice
                # check for duplicated characters
                    # if the characters are unique update the answer
        # return the answer
```

**Sliding Window**
- [Source code](source/SlidingWindow.py)
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # set a hashset
        # set the return variable
        # loop until start or end exceeds the limit
            # if end pointer is unique
                # record the end character in the hashset
                # increase the end pointer
                # record the maximum return value
            # if the right pointer is a duplicate
                # remove the the start character from the hashset
                # increase the start pointer
        # return the answer
```

**Sliding Window Optimized**
- [Source code](source/SlidingWindowOpt.py)
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # set a hashset
        # set the return variable
        # loop until the end exceeds the limit
            # if the end character is a duplicate
                # move the start to the duplicated character
            # increment the end pointer
            # update the maximum length
            # record the duplicated character with the future starting point
        # return the answer
```
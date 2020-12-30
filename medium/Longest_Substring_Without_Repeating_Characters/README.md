### Longest Substring Without Repeating Characters

**Sliding Window**
- Concepts 
    - Implement a sliding window that uses two pointers left and right
        - Increase the right if there are no duplicates 
        - Increase the left until there are no duplicates in the window
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
        pass
```

**Sliding Window Optimized**
- Concepts
    - Considering the case `a [b] c a b [b] f g`
        - There is no point for the left pointer to increment one by one
        - The left pointer can skip to `a b c a b [b] [f] g` 
- [Source code](source/SlidingWindowOpt.py)
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # set a hashmap
        # set the return variable
        # loop until the end exceeds the limit
            # if the end character is a duplicate
                # move the start to the duplicated character
            # increment the end pointer
            # update the maximum length
            # record the duplicated character with the future starting point
        # return the answer
        pass
```
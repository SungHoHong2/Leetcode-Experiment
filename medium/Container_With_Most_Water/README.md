### Container With Most Water
**Two Pointer Approach**
- [Source code](source/TwoPointer.py)
```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # set the variable the check the maximum area
        # set the pointer of the left
        # set the pointer of the right
        # iterate until the items from the list are checked
            # get the shortest height from the left and right
            # update the maximum area of the height
            # if the left side is shorter
                # move from the left
            # if the right side is shorter
                # move from the right
        # return the maximum area
```
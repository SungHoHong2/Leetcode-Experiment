### Two Sum II - Input array is sorted
**Two Pointers**
- [Source code](source/)
```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # set the two indexs from left and right
        # loop until the two pointers converge
            # calculate the sum of the leftmost and the rightmost value
            # if the results are equal to the target
                # return the indexes
            # if the results are smaller than the target
                # increase the leftmost pointer
            # if the results are bigger than the target
                # decrease the rightmost pointer
        # return [-1,-1] if there is no match
```
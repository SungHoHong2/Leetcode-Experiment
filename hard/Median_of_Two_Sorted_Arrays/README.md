### Median of Two Sorted Arrays
**Binary Search**
- [Concepts](images/Binary.png)
- [Source code](source/Binary.py)
- [Reference #1](https://www.youtube.com/watch?v=LPFhl65R7ww&t=1013s)
```python
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # search from the smallest array
        # get the length of array x
        # get the length of array y
        # set the low and high pointer for binary search in array x
        # invoke the binary search
        # x [       maxLeft | minRight     ]
        # y [                 maxLeft | minRight     ]
            # get the length of the partition of array x
            # get the length of the partition of array y that is same as partition of array x
            # ex) the less items in array x, more items need to go to array y
            # update the index for left partition
            # update the index for right partition
            # partitioned the array at the correct place
                # return the result when the length of the whole array is even
                # return the result when the length of the whole array is odd
            # shrink the leftside partition
            # shrink the rightside partition
            pass
```


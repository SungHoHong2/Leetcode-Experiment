### Merge Sorted Array
**Merge and sort**
- [source_code](source/recursive.py)
```python
class Solution(object):
    # define a recursive merge sort
        # if the array is more than one element
            # find the middle of the array
            # create a temporary left array
            # create a temporary right array
            # run recursive for the left array
            # run recursive for the right array
            # set the index for left array, right array and return array
            # loop until left or right is depleted
                # if left is smaller than right
                    # left goes to the return array
                    # increase the index of the left
                # if right is smaller than left 
                    # right goes to the return array
                # increase the index of the return array
            # empty the left array
            # empty the right array
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        # append the two array 
        # invoke the mergesort function
```

**Two pointers / Start from the beginning**
- [source code](source/begin.py)
```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # make a copy of nums1
        # empty the nums1(return array)
        # Two get pointers for nums1 and nums2.
        # iterate until the nums1 or the num2 are empty
            # if nums1 is smaller
                # append nums1 to return array
                # increaese the index of nums1
            # if nums2 is smaller
                # append nums2 to return array
                # increase the index of nums2
        # if nums1 is not empty
            # append nums1 to the return array
        # if nums2 is not empty
            # append nums2 to the return array
```

**Two pointers / Start from the end**
- [source code](source/end.py)
```python
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        # two get pointers for nums1 and nums2
        # set pointer for nums1
        # while there are still elements to compare
            # if tail of the nums1 is smaller than the tail of the nums2
                # append nums2 tail first
                # decrease the index
            # if the tail of the nums2 is smaller than the nums1
                # append nums1 tail first
                # decrease the index of nums1
            # decrease the index of the return array 
        # add missing elements from nums2
```
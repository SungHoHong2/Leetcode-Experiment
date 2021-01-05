### K Closest Points to Origin
**Sort**
- Concepts
    - Sort the the points according to the distance
    - Return `K`th closest points
- [Source code](source/Sort.py)
```python
class Solution(object):
    def kClosest(self, points, K):
        # sort the array based on the euclidean distance to the original point 
        # return the kth amount of the list
        pass
```

**Quick Sort**
- [Concepts](images/divide.png)
    - Apply the same tactic while implementing the quick-sort from scratch
    - Sort until Kth number of items are sorted to the left
- [Quick Sort v2](source/Quicksort2.py)
```python
class Solution(object):
    def kClosest(self, points, K):
        def dist(i):
            pass
    
        def sort(left, right, K):
            # return when recursion tree reaches the leaf
            # find the random pivot index
            # place the pivot in the front of the array
            # parition the index based on the random pivot and get the pivot index
            # if the number of elements in the leftside is more than K
                # reduce the scope of the return by sorting out the left side of the input
            # if the number of elements of the left side is less than K 
                # increase the scope of the return by sorting the right side of the input
            pass

        def partition(left, right):
            # set the pivot and the left index 
            # quick-sort the elements using the pivot 
                # increment from left if the distance is smaller than the pivot's
                # decrement from right if the distance is larger than the pivot's
                # break if the sorting is complete
                # swap the incompatible distances between left and right
            # swap the pivot with the recently swapped leftside distance
            # return middle index
            pass
        
        # invoke sort function
        # return the kth amount of sorted result
        pass
```


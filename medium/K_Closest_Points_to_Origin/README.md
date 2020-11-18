### K Closest Points to Origin
**Sort**
- [Source code](source/Sort.py)
```python
class Solution(object):
    def kClosest(self, points, K):
        # sort the array based on the euclidean distance to the original point 
        # return the kth amount of the list
        pass
```

**Divide and Conquer**
- [Concepts](images/divide.png)
- [Source code](source/Recursive.py)
```python
class Solution(object):
    def kClosest(self, points, K):
        # create a lambda function that calculates the euclidean distance        
        def sort(i, j, K):
            # return when recursion tree reaches the leaf
            # find the random pivot index
            # place the pivot in the front of the array
            # parition the index based on the random pivot and get the pivot index
            # if the number of elements in the leftside is more than K 
                # sort recursively from the left array
            # if the number of elements of the left side is less than K 
                # explore more elements in the right side just enough to match the K
            pass

        def partition(i, j):
            # save the pivot index
            # get the distance of the pivot
            # quick-sort the elements using the pivot 
            while True:
                # increment from left if the distance is smaller than the pivot's
                # decrement from right if the distance is larger than the pivot's
                # break if the sorting is complete
                # swap the incompatible distances between left and right
                pass
            # swap the pivot with the recently swapped leftside distance
            # return middle index
            pass
        # invoke sort function
        # return the kth amount of sorted result
        pass
```


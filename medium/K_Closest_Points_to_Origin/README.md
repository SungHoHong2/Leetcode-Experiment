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
            # get the pivot index that will sort array A[ i...pivot...j ]
            # place the pivot in the front of the array A[ pivot.i....j ]
            # return the partitioned index A[i] <= A[mid] <= A[j]
            # if the number of Kth element is smaller than the partitioned index
                # sort recursively from the left array
            # if the number of kth element is bigger than the partitioned index
                # sort recursively from the right array
            pass

        def partition(i, j):
            # save the pivot index
            # get the distance value of the pivot
            # move to the index that needs to be sorted
            # loop until the sorting is complete
                # increment from left if the distance of ith index is smaller than the pivot
                # increment from right if the distance of ith index is bigger than the pivot
                # break if the sorting is complete
                # place the smaller value to the leftside and bigger value to the rigtside of the pivot
            # move the pivot value to the middle index
            # return middle index
            pass

        # invoke sort function
        # return the kth amount of sorted result
```


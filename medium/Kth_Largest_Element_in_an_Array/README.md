- **Heap**
    - [source code](source/heap.py)
```python
from heapq import heappush, heappop
class Solution:
    def findKthLargest(self, nums, k):
        # push the input to the heap 
        # get the kth largest number
        pass
```

- **QuickSort**
    - [concepts](image/quicksort.png)
    - [source code](source/quicksort.py)
```python
class Solution:
    def findKthLargest(self, nums, k):

        def partition(left, right):
            # find the random pivot index and the value
            # get the value of the pivot
            # temporary hide the pivot value in the rightmost side 
            # move all the values than the pivot behind the middle
            # recover the pivot value from the rightmost side
            # return the index of the middle
            pass

        def qsort(left, right, K):
            # return the item if the recursion reach the leaf 
            # get the index of the pivot from the partition
            # if the index of the pivot is the Kth smallest 
                # return the value 
            # if pivot is bigger than the kth smallest 
                # search the leftside 
            # if the pivot is smaller than the kth smallest 
                # search the rightside
            pass
            
        # return the kth largest value from the quicksort
        pass
```
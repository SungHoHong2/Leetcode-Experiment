- **Heap**
    - [source code](source/heap.py)
```python
class Solution:
    def findKthLargest(self, nums, k):
        # use the nlargest in the heapq 
        pass 
```

- **QuickSort**
    - [concepts](image/quicksort.png)
    - [source code](source/quicksort.py)
```python
class Solution:
    def findKthLargest(self, nums, k):
        def partition(left, right, pivot_index):
            # get the value of the pivot 
            # 1. move pivot to end
            # 2. move all smaller values to the leftside
            # 3. move pivot to its final place
            # return the index of the pivot 
            pass

        def select(left, right, k_smallest):
            # return the item if the recursion reach the leaf 
            # select a random pivot_index between
            # get the index of the pivot from the partition
            # if the index of the pivot is the Kth smallest 
                # return the value 
            # if pivot is bigger than the kth smallest 
                # search the leftside 
            # if the pivot is smaller than the kth smallest 
                # search the rightside
            pass
            
        # invoke the recursion [ kth largest = (n - k)th smallest ]
        pass
```
### Merge k Sorted Lists

**Compare one by one**
- [Source code](source/Compare.py)
```python
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # set the pointers for the returning linked-list
        # set current pointers for all the lists
        # loop until all the items in the lists are computed
            # get the smallest number and the index of the list that the number is in it
            # break the loop if all the lists are empty
            # add the answer to the returning linked-list
            # update the pointer of the returning linked-list 
            # deplete the smallest item from the chosen list
        # return the result
        pass
```

**Priority Queue**
- [Source code](source/Priority.py)
```python
from heapq import heappush, heappop

class Solution(object):
    def mergeKLists(self, lists):
        # set the pointers for the returning linked-list
        # set the priority queue min-heap 
        # append all the inputs from the lists to the priority queue
        # pop numbers from the min-heap and create the linked-list
        # return the sorted linked-list
        pass
```

**Merge with Divide And Conquer**
- Concept 
    - Merge the lists by neighbors
      - `merged = (0),(1),(2),(3),(4)`
      - `merged = (0,1),(2,3),(4)`
      - `merged = ((0),(2)),(4)`
      - `merged = ((0),(4))`
- [Source code](source/Merge.py)
```python
class Solution(object):
    def mergeKLists(self, lists):
        # get the total number of lists 
        # set the pointer to merge the neighboring lists 
        # loop until the lists become a single list 
            # iterate two lists per loop
                # merge the neighboring lists
            # increase the size of the combined neighbors 
        # return the merged list
        pass
    
    def merge(self, l1, l2):
        # set the pointers of the returning linked-list 
        # loop until one of the linked list is depleted
            # append the smaller number from the two lists 
        # append with second if the first is empty  
        # append the first if the second is empty
        # return the linked-list
        pass
```

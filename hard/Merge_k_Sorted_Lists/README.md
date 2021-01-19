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
    - Merge neighbors recursively
- [Source code v2](source/Merge2.py)
- [Source code v1](source/Merge.py)
```python
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # start divide and conquer
        pass 
        
    def merge(self, lists):
        # return nothing if there are no more linked-lists 
        # return the head if the recursion reaches a single linked-list 
        # collect the two linked list from the divide and conquer 
        # merge & sort the two linked-list in an ascending order
        # return the head of the merged linked-list 
        pass      
```

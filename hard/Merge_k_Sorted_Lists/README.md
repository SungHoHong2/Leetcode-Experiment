### Merge k Sorted Lists
**Brute Force**
- [Source code](source/Brute.py)
```python
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # set the array for storing all the lists
        # set the fake header and the current pointer
        # iterate all the lists
            # append the items to the total array
        # sort the array and create the returning linked-list
        # return the result
```

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

**Optimize Approach 2 by Priority Queue**
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

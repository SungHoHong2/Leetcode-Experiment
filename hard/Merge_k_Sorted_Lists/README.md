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
        # set the fake header and the current pointer
        # set current pointers for all the lists
        # compare all the lists one item at a time and add the smallest item for the result
        # return the result
```

**Optimize Approach 2 by Priority Queue**
- [Source code](source/Priority.py)

**Merge with Divide And Conquer**
- [Source code](source/Merge.py)

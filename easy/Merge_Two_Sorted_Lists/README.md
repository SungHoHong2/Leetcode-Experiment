# Merge Two Sorted Lists

**Iteration**
- [source code](source/iteration.py)

```python
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        # create a fake node to use as return header

        # loop until both l1 and l2 are empty
            # if l1 is smaller than l2
                # connect l1 to the return header
                # pop the l1 array
            # if l2 is smaller than l1
                # connect l2 to the return header
                # pop the l2 array
            # move on to the next return header

        # connect the rest to the return header

        # return the header
```


**Recursive**
- [source code](source/recursive.py)
```python 
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        # if l1 is empty
            # return the l2 array

        # if l2 is empty
            # return the l1 array

        # if l1 is smaller than l2
            # l1 goes first

        # if l2 is smaller than l1
            # l2 goes is first
```

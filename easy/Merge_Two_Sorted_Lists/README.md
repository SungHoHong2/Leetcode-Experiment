# Merge Two Sorted Lists

**Recursive**
- [source code](source/recursive.py)
- Time complexity : **O(n+m)** 
    - each recursive call increments the pointer to l1 or l2 by one
    - there will be `exactly one call` to mergeTwoLists per element in each list 
    - the time complexity is `linear` in the combined size of the lists
- Space complexity : **O(n+m)**
    - `first call to mergeTwoLists` does not return until the ends of both l1 and l2 have been reached
    - n+m stack frames consume O(n + m)O(n+m) space.
    
```python 
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        # (halting recursive fucntion)
        # if l1 is empty
            # return the l2 array
        # if l2 is empty
            # return the l1 array

        # (returning array)
        # if l1 is smaller than l2
            # l1 goes first
            # return l1 
        # if l2 is smaller than l1
            # l2 goes is first
            # return l2
```

**Iteration**
- [source code](source/iteration.py)
- Time complexity : **O(n+m)**
    - exactly one of l1 and l2 is incremented on each loop iteration
- Space complexity : **O(1)**
    - only allocates a few pointers
    - constant overall memory footprint

```python
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        # create a fake node to use as return header

        # loop until either l1 or l2 are empty
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


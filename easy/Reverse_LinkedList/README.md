### Reverse Linked List
**Recursive**
- [concepts](images/recursive.png)
- [source code](source/recursive.py)
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # reached the final node
            # return the final node (return value)
        # invoke the recursive function
        # reverse the order of the current node and the next node
        # disable the pointer of the current node (this part will be updated by the previous recursive function)
        # return the final node (return value)
```

**Iteration**
- [source code](source/iteration.py)
```python
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # set the previous node
        # set the current node
        # loop until the current node reaches the end
            # save the pointer for the next node
            # point the current node to the previous node
            # set the previous node to the current node
            # move on to the next node
        # return the new head
```

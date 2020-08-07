### Reverse Linked List
**Recursive**
- [Concepts](images/recursive.png)
- [Source code](source/recursive.py)
- Time complexity : **O(n)** Assume that nn is the list's length
- Space complexity : **O(n)** The extra space comes from implicit stack space due to recursion

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
- [Source code](source/iteration.py)
- Time complexity : **O(n)** Assume that nn is the list's length
- Space complexity : **O(1)**

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

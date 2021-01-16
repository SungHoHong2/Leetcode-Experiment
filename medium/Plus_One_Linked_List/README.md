### Plus One Linked List
**Sentinel**
- [Source code](source/Sentinel.py)
```python
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        # sentinel head [0,9,9,9]
        # find the rightmost not-nine digit [(0),9,9,9]
        # increase this rightmost not-nine digit by 1 [(1),9,9,9]
        # set all the following nines to zeros [(1),0,0,0]
        # return the whole linked-list if the sentinel is updated or return without the sentinel
        pass
```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # set the array for storing all the lists
        total = list()
        # set the fake header and the current pointer
        head = point = ListNode(-1)
        # iterate all the lists
        for l in lists:
            # append the items to the total array
            while l:
                total.append(l.val)
                l = l.next
        # sort the array and create the returning linked-list
        for x in sorted(total):
            point.next = ListNode(x)
            point = point.next
        # return the result
        return head.next
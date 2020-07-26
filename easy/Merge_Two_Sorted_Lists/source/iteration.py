# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        # create a fake node to use as return header
        prevHead = ListNode(-1)
        prev = prevHead

        # loop until either l1 or l2 are empty
        while l1 and l2:
            # if l1 is smaller than l2
            if l1.val < l2.val:
                # connect l1 to the return header
                prev.next = l1
                # pop the l1 array
                l1 = l1.next
            # if l2 is smaller than l1
            else:
                # connect l2 to the return header
                prev.next = l2
                # pop the l2 array
                l2 = l2.next
            # move on to the next return header
            prev = prev.next

        # connect the rest to the return header
        prev.next = l1 if l1 else l2

        # return the header
        return prevHead.next

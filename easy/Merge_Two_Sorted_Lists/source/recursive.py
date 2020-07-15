# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def mergeTwoLists(self, l1, l2):

        # if l1 is empty
        if l1 is None:
            # return the l2 array
            return l2

        # if l2 is empty
        elif l2 is None:
            # return the l1 array
            return l1

        # if l1 is smaller than l2
        elif l1.val < l2.val:
            # l1 goes first
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        # if l2 is smaller than l1
        else:
            # goes is first
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

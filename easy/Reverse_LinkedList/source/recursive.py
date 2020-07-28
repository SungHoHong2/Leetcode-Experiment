# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # reached the final node
        if head == None or head.next == None:
            # return the final node
            return head

            # invoke the recursive function
        p = self.reverseList(head.next)

        # reverse the order of the current node and the next node
        head.next.next = head

        # disable the pointer of the current node (this part will be updated by the previous recursive function)
        head.next = None

        # return the final node
        return p
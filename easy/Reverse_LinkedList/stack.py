# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        stack = []
        node = head
        while node != None:
            # print(node.val)
            stack.append(node)
            node = node.next

        if len(stack) == 0:
            return node

        rtn = stack.pop()
        prev = rtn
        # print(prev.val)

        while len(stack) != 0:
            prev.next = stack.pop()
            prev = prev.next
            # print(prev.val)

        prev.next = None
        return rtn
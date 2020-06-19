# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = cur = ListNode(0)
        c = 0

        while l1 or l2:
            tmp = c
            if l1:
                tmp += l1.val
                l1 = l1.next
            if l2:
                tmp += l2.val
                l2 = l2.next

            c = tmp / 10
            tmp = tmp % 10
            cur.next = ListNode(tmp)
            cur = cur.next

        if c:
            cur.next = ListNode(c)
            cur = cur.next

        return result.next

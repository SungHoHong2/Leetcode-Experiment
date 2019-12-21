# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        arr = []

        result = cur = ListNode(0)
        tmp = head

        while tmp != None:
            arr.append(tmp)
            tmp = tmp.next

        arr.reverse()
        for item in arr:
            cur.next = item
            cur = cur.next
        cur.next = None
        return result.next


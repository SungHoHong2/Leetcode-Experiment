"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head
        cur = head

        while cur:
            ncur = Node(cur.val)
            ncur.next = cur.next
            cur.next = ncur
            cur = cur.next.next

        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            else:
                cur.next.random = None

            cur = cur.next.next

        ncur = head.next
        cur = head
        new = head.next

        while cur:
            cur.next = cur.next.next
            if ncur.next:
                ncur.next = ncur.next.next

            else:
                ncur.next = None
            ncur = ncur.next
            cur = cur.next

        return new


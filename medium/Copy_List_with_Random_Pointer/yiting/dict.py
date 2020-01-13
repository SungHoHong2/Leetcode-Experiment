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

        dict = collections.defaultdict(lambda: Node(0))
        dict[None] = None
        n = head
        while n:
            dict[n].val = n.val
            dict[n].next = dict[n.next]
            dict[n].random = dict[n.random]
            n = n.next
        return dict[head]

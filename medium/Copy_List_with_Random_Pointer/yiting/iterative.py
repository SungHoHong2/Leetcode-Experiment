"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution(object):
    def __init__(self):
        self.visited = {}

    def update(self, head):
        if not head:
            return None
        if head in self.visited:
            return self.visited[head]
        node = Node(head.val)
        self.visited[head] = node
        return self.visited[head]

    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head

        cur = head

        while cur:
            ncur = self.update(cur)
            ncur.next = self.update(cur.next)
            ncur.random = self.update(cur.random)
            cur = cur.next
            ncur = ncur.next

        return self.visited[head]
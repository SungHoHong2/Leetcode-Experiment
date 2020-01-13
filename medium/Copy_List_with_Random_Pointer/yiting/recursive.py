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

    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        if head in self.visited:
            return self.visited[head]
        node = Node(head.val)
        self.visited[head] = node
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)

        return node
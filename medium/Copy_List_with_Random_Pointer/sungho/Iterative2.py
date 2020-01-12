"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':

        if not head:
            return None

            # attach the cloned nodes
        ptr = head
        while ptr:
            newNode = Node(ptr.val, None, None)
            newNode.next = ptr.next
            ptr.next = newNode
            ptr = newNode.next

            # attach the random from the cloned nodes
        ptr = head
        while ptr:
            if ptr.random:
                ptr.next.random = ptr.random.next
            else:
                ptr.next.random = None

            ptr = ptr.next.next

            # get only the new nodes and return
        ptr_new = head.next

        while ptr_new:
            ptr_new.next = ptr_new.next.next if ptr_new.next else None
            ptr_new = ptr_new.next

        return head.next
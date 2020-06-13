"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):

    def flatten(self, head):

        if not head:
            return head

        # create a pseudo head for the (prev)
        pseudoHead = Node(None, None, head, None)

        # run the recursive function (prev, next)
        self.flatten_dfs(pseudoHead, head)

        # detach the pseudo head from the real head
        pseudoHead.next.prev = None

        # return the real head
        return pseudoHead.next

    def flatten_dfs(self, prev, curr):
        """ return the tail of the flatten list """

        # reached the deadend of the queue
        if not curr:
            # return the tail of the node
            return prev

        # connect the prev and the curr node
        curr.prev = prev
        prev.next = curr

        # get the pointer to the right node
        tempNext = curr.next

        # flatten the child queue (the left node)
        tail = self.flatten_dfs(curr, curr.child)

        # remove the child node
        curr.child = None

        # flatten the right node and connect them with the tail of the child queue
        return self.flatten_dfs(tail, tempNext)
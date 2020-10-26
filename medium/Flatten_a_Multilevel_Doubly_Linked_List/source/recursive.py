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
        # return none if there is no input
        if not head:
            return head
        # create a fake head
        pseudoHead = Node(None, None, head, None)
        # run the recursion (prev, next)
        self.flatten_dfs(pseudoHead, head)
        # detach the pseudo head from the real head
        pseudoHead.next.prev = None
        # return the real head
        return pseudoHead.next

    def flatten_dfs(self, prev, curr):
        """ return the tail of the flatten list """
        # return the tail if the recursion reached its leaf
        if not curr:
            return prev
        # connect the previous and the current node
        curr.prev, prev.next = prev, curr
        # get the pointer to the right node
        tempNext = curr.next
        # connect the current node with its children by using recursion
        tail = self.flatten_dfs(curr, curr.child)
        # remove the child node of the current node
        curr.child = None
        # connect the last child with the right node by using recursion
        return self.flatten_dfs(tail, tempNext)
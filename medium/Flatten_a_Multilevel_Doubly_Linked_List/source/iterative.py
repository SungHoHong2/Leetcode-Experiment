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
        # return nothing if there is no input
        if not head:
            return
        # create a fake head
        pseudoHead = Node(0, None, head, None)
        # assign the fake head the prev
        prev = pseudoHead
        # generate a stack
        stack = []
        # append the real head
        stack.append(head)
        # iterate through the stack
        while stack:
            # pop the latest inserted node
            curr = stack.pop()
            # connect the previous and the current node
            prev.next = curr
            curr.prev = prev
            # push the next node into the stack
            if curr.next:
                stack.append(curr.next)
            # push the child node into the stack
            if curr.child:
                stack.append(curr.child)
                # remove the child pointer of the current node
                curr.child = None
            # set the current node as the previous node
            prev = curr
        # detach the pseudo head node from the result.
        pseudoHead.next.prev = None
        # return the flattened list
        return pseudoHead.next
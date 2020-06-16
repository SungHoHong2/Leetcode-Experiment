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
            return

        # generate a fake head
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

            # create curr.prev
            prev.next = curr
            curr.prev = prev

            # push the curr.next to the stack
            if curr.next:
                stack.append(curr.next)

            # if the curr has the left node
            # since this is a stack the left node will be popped at the next iteration
            if curr.child:
                stack.append(curr.child)
                # don't forget to remove all child pointers.
                curr.child = None

            prev = curr

        # detach the pseudo head node from the result.
        pseudoHead.next.prev = None
        return pseudoHead.next
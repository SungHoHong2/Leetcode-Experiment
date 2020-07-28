class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # set the previous node
        prev = None
        # set the current node
        curr = head
        # loop until the current node reaches the end
        while curr != None:
            # save the pointer for the next node
            nextTemp = curr.next
            # point the current node to the previous node
            curr.next = prev
            # set the previous node to the current node
            prev = curr
            # move on to the next node
            curr = nextTemp
        # return the new head
        return prev

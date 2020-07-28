class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        prev = None
        curr = head

        while curr != None:
            nextTemp = curr.next
            curr.next = prev
            prev = curr
            curr = nextTemp

        return prev
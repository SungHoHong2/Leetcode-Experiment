# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        # create return array
        head = ListNode(0)

        # pointer that will be used for the iteration
        curr = head

        # initialize the carry
        carry = 0

        # iterate until either l1 or l2 are empty
        while l1 != None or l2 != None:

            # initialize x, y
            x = y = 0

            # if l1 is not empty assign x as l1.val
            if l1:
                x = l1.val
                l1 = l1.next

            # if l2 is not empty assign y as l2.val
            if l2:
                y = l2.val
                l2 = l2.next

            # get the sum value
            sum = x + y + carry

            # get the carry value for the next iteration
            carry = sum // 10

            # add the answer
            curr.next = ListNode(sum % 10)

            # move on to next iteration
            curr = curr.next

        # send the carry value to the next node just in case this is the end of the iteration
        if carry > 0:
            curr.next = ListNode(carry)

        # return the result without the dummy head
        return head.next

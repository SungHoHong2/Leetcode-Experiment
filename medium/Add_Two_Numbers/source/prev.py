class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        # create the return linked list
        head = ListNode(0)

        # initialize the carry
        carry = 0

        # initialize the pointer used during the iteration
        curr = head

        # track the previous pointer to remove the NULL node
        prev = None

        # iterate until l1 or l2 is empty
        while l1 != None or l2 != None:

            # calculate the current nodes
            x, y = 0, 0

            if l1:
                x = l1.val
                l1 = l1.next

            if l2:
                y = l2.val
                l2 = l2.next

            sum = carry + x + y
            carry = sum // 10
            curr.val = sum % 10

            # just in case this is the last iteration, and there is a carry
            if carry > 0:
                curr.next = ListNode(carry)

            # initialize the node for the next iteration
            else:
                curr.next = ListNode(0)

            # track the previous pointer
            prev = curr

            # proceed to the next iteration
            curr = curr.next

            # use the prev to sever the NULL node
        if curr.val == 0:
            prev.next = None

            # return the result
        return head



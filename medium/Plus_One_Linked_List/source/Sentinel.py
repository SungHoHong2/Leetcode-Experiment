class Solution:
    def plusOne(self, head: ListNode) -> ListNode:

        # sentinel head [0,9,9,9]
        sentinel = ListNode(0)
        sentinel.next = head
        not_nine = sentinel

        # find the rightmost not-nine digit [(0),9,9,9]
        while head:
            if head.val != 9:
                not_nine = head
            head = head.next

        # increase this rightmost not-nine digit by 1 [(1),9,9,9]
        not_nine.val += 1
        not_nine = not_nine.next

        # set all the following nines to zeros [(1),0,0,0]
        while not_nine:
            not_nine.val = 0
            not_nine = not_nine.next

        # return the whole linked-list if the sentinel is updated or return without the sentinel
        return sentinel if sentinel.val else sentinel.next
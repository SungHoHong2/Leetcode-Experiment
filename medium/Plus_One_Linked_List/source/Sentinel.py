class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        # create the sentinel head
        sentinel = ListNode(0, head)
        curr = sentinel.next
        not_nine = None
        # find the rightmost not-nine digit
        while curr:
            if curr.val != 9:
                not_nine = curr
            curr = curr.next
        # increase this rightmost not-nine digit by 1 if the not_nine is found
        if not_nine:
            not_nine.val += 1
            curr = not_nine.next
        # increase the sentinel by 1 if the not-nine digit is not found
        else:
            sentinel.val += 1
            curr = sentinel.next
        # set all the following nines to zeros
        while curr:
            curr.val = 0
            curr = curr.next
        # return the whole linked-list if the sentinel is updated or return without the sentinel
        return sentinel if sentinel.val != 0 else sentinel.next
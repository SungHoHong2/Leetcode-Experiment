# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        mergedList = None
        rtnHeader = None
        leftover = None

        while True:

            cmp1 = cmp2 = float("inf")

            if l1:
                cmp1 = l1.val
            else:
                leftover = l2
                break

            if l2:
                cmp2 = l2.val
            else:
                leftover = l1
                break

            # print(rtnHeader)

            if cmp1 < cmp2:
                # print(cmp1)

                if rtnHeader is None:
                    mergedList = ListNode(cmp1)
                    rtnHeader = mergedList
                else:
                    mergedList.next = ListNode(cmp1)
                    mergedList = mergedList.next

                l1 = l1.next
            else:
                # print(cmp2)

                if rtnHeader is None:
                    mergedList = ListNode(cmp2)
                    rtnHeader = mergedList
                else:
                    mergedList.next = ListNode(cmp2)
                    mergedList = mergedList.next

                l2 = l2.next

        # print the left overs
        while True:

            if leftover is None:
                break

            if rtnHeader is None:
                mergedList = ListNode(leftover.val)
                rtnHeader = mergedList
            else:
                mergedList.next = ListNode(leftover.val)
                mergedList = mergedList.next

            leftover = leftover.next

        # print(rtnHeader)
        return rtnHeader





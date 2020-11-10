# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # set the fake header and the current pointer
        head = point = ListNode(-1)
        # set current pointers for all the lists
        headers = [i for i in lists]
        # compare all the lists one item at a time and add the smallest item for the result
        while True:
            idx, smallest = -1, float('inf')
            for i in range(len(headers)):
                if headers[i]:
                    if smallest > headers[i].val:
                        smallest = headers[i].val
                        idx = i
            if idx == -1:
                break
            point.next = ListNode(headers[idx].val)
            point = point.next
            headers[idx] = headers[idx].next
        # return the result
        return head.next
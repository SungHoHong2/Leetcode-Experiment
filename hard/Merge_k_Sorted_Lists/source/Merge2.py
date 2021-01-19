class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # start divide and conquer
        return self.merge(lists)

    def merge(self, lists):
        # return nothing if there are no more linked-lists
        if len(lists) == 0:
            return
        # return the head if the recursion reaches a single linked-list
        if len(lists) == 1:
            return lists[0]
        # collect the two linked list from the divide and conquer
        mid = len(lists) // 2
        l1 = self.merge(lists[:mid])
        l2 = self.merge(lists[mid:])
        # merge & sort the two linked-list in an ascending order
        head = curr = ListNode(-1)
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l2 if not l1 else l1
        # return the head of the merged linked-list
        return head.next
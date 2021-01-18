class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # set the pointers for thee returning linked-list
        head = point = ListNode(-1)
        # set current pointers for all the lists
        headers = [i for i in lists]
        # loop until all the items in the lists are computed
        while True:
            # get the smallest number and the index of the list that the number is in it
            idx, smallest = -1, float('inf')
            for i in range(len(headers)):
                if headers[i] and smallest > headers[i].val:
                    smallest = headers[i].val
                    idx = i
            # break the loop if all the lists are empty
            if idx == -1:
                break
            # add the answer to the returning linked-list
            point.next = ListNode(headers[idx].val)
            # update the pointer of the returning linked-list
            point = point.next
            # deplete the smallest item from the chosen list
            headers[idx] = headers[idx].next
        # return the result
        return head.next
from heapq import heappush, heappop

class Solution(object):
    def mergeKLists(self, lists):
        # set the pointers for the returning linked-list
        head = curr = ListNode(-1)
        # set the priority queue min-heap
        pq = list()
        # append all the inputs from the lists to the priority queue
        for l in lists:
            while l:
                heappush(pq, l.val)
                l = l.next
        # pop numbers from the min-heap and create the linked-list
        while pq:
            curr.next = ListNode(heappop(pq))
            curr = curr.next
        # return the sorted linked-list
        return head.next
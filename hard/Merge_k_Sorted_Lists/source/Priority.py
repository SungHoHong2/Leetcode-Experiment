class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = point = ListNode(0)
        # q = PriorityQueue()
        heap = list()
        heapq.heapify(heap)

        for l in lists:
            while l:
                heapq.heappush(heap, l.val)
                l = l.next

        while heap:
            point.next = ListNode(heapq.heappop(heap))
            point = point.next

        return head.next
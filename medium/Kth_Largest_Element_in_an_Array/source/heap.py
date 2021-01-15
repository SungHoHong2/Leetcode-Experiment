from heapq import heappush, heappop
class Solution:
    def findKthLargest(self, nums, k):
        # push the input to the heap
        pq = list()
        for num in nums:
            heappush(pq, num)

        # get the kth largest number
        kth = len(nums) - k
        while pq:
            if not kth:
                return heappop(pq)
            else:
                heappop(pq)
            kth -= 1
class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        import heapq
        heap = []
        for p in points:
            dist = -(p[0] ** 2 + p[1] ** 2)
            if len(heap) == K:
                heapq.heappushpop(heap, (dist, p))
            else:
                heapq.heappush(heap, (dist, p))

        return [p for (dist, p) in heap]

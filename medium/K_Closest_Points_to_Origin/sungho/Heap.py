class Solution(object):
    def kClosest(self, points, K):
        import heapq
        heap = []
        for p in points:
            x, y = p[0], p[1]
            dist = -(x*x + y*y)
            if len(heap) == K:
                heapq.heappushpop(heap, (dist, p))
            else:
                heapq.heappush(heap, (dist, p))
        return [p for (dist, p) in heap]
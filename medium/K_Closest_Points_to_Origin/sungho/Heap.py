class Solution(object):
    def kClosest(self, points, K):
        import heapq
        heap = []

        # iterate all the points
        for p in points:

            # get the first x and y value
            x, y = p[0], p[1]

            #  get the distance
            dist = -(x * x + y * y)

            # if the elements in the heap is more than than K
            if len(heap) == K:
                # pop out the heap and push the current heap
                heapq.heappushpop(heap, (dist, p))
            else:
                # if the elements in the heap is less than K
                # push the elements in the heap
                heapq.heappush(heap, (dist, p))

        # return the heap into an array
        return [p for (dist, p) in heap]
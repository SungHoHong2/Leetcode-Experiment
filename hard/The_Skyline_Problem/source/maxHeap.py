from heapq import heappush, heappop

class Solution(object):
    def getSkyline(self, buildings):
        # add starting point of the building (L, -H, R)
        events = [(L, -H, R) for L, R, H in buildings]
        # add ending point of the building (R,0,0)
        events += [(R, 0, 0) for _, R, _ in buildings]
        # sort the events in ascending order based on the L
        events.sort()
        # set the returning array that collects [L, height] with a starting point
        res = [[0, 0]]
        # set the max heap that collects the [-height, R]
        pq = [(0, float("inf"))]
        # iterate the building
        for L, H, R in events:
            # get the latest building from the heap
            pq_height, pq_right = pq[0]
            # pop buildings that has ended
            while pq_right <= L:
                heappop(pq)
                pq_height, pq_right = pq[0]
            # push the building to the heap
            if H:
                heappush(pq, (H, R))
            # get the latest building from the returning array
            res_left, res_height = res[-1]
            # get the latest building from the heap
            pq_height, pq_right = pq[0]
            # append the result if the tallest building changes
            if res_height != -pq_height:
                res.append((L, -pq_height))
        # return the result without the starting point
        return res[1:]

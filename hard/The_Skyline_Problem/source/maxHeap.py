from heapq import heappush, heappop
class Solution(object):
    def getSkyline(self, buildings):
        # add starting point of the building (L, -H, R)
        events = [(L, -H, R) for L, R, H in buildings]
        # add ending point of the building events (R,0,0)
        events += list({(R, 0, 0) for _, R, _ in buildings})
        # sort the events in ascending order based on the left
        events.sort()
        # set the result [L, height] with a starting point
        res = [[0, 0]]
        # set the min heap to keep track of the highest height, [-height, R]
        tallest = [(0, float("inf"))]
        # iterate the building
        for L, negH, R in events:
            # pop buildings that no longer valid
            while tallest[0][1] <= L:
                heappop(tallest)
            # keep track of the valid building with the tallest height
            if negH:
                heappush(tallest, (negH, R))
            # append the result if the tallest building changes
            if res[-1][1] != -tallest[0][0]:
                res += [ [L, -tallest[0][0]] ]
        # return the result without the starting point
        return res[1:]
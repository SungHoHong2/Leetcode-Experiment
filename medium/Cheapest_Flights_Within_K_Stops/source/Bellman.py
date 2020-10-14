class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        # create two arrays for storing distances and swapping
        distances = [[float('inf')] * n for _ in range(2)]
        # set the distnace of the origin node to zero
        distances[0][src] = distances[1][src] = 0
        # K + 1 iterations of Bellman Ford
        for iterations in range(K + 1):
            # Iterate K times
            for s, d, w in flights:
                # even number & 1  = 0, odd number & 1 = 1
                print(iterations, 1 - iterations&1, iterations&1)
                # get the total distance of the "origin" from the previous array
                prev = distances[1 - iterations&1][s]
                # get the total distance of the destination from the current array
                new = distances[iterations&1][d]
                # if the newly added weight
                if prev + w < new:
                    # update the current destination
                    distances[iterations&1][d] = prev + w
        # return -1 if the Kth destination is not reachable, else return the shortest distance
        return -1 if distances[K&1][dst] == float("inf") else distances[K&1][dst]
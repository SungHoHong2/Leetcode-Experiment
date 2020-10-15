class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        # create two arrays for storing distances and swapping
        distances = [[float('inf') for i in range(n)] for j in range(2)]
        # set the distances of the origin node to zero
        distances[0][src] = distances[1][src] = 0
        # K + 1 iterations of Bellman Ford
        for iteration in range(K+1):
            # get the start, dest, and weight from each flight and use iteration&1 to swap between even=0 to odd=1
            for s, d, w in flights:
                # get the total distance of the start from the previous array
                prev = distances[1-iteration&1][s]
                # get the total distance of the dest from the current array
                curr = distances[iteration&1][d]
                # if the newly added weight
                if prev + w < curr:
                    # update the current destination
                    distances[iteration&1][d] =  prev + w
        # return -1 if the Kth destination is not reachable, else return the shortest distance
        return -1 if distances[K&1][dst] == float("inf") else distances[K&1][dst]
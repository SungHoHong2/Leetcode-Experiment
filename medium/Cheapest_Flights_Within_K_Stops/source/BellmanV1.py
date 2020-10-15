class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        # create the whole array for storing distances and swapping
        distances = [[float('inf') for i in range(n)] for j in range(K+2)]
        # set the distances of the origin node to zero
        distances[0][src] = 0
        # K + 1 iterations of Bellman Ford
        for iteration in range(1,K+2):
            # update all the flights from the previous result
            for s, d, w in flights:
                distances[iteration][s]  = distances[iteration-1][s]
                distances[iteration][d]  = distances[iteration-1][d]
            # update the new distances
            for s, d, w in flights:
                # get the total distance of the start from the previous array
                prev = distances[iteration-1][s]
                # get the total distance of the dest from the current array
                curr = distances[iteration][d]
                # if the newly added weight
                if prev + w < curr:
                    # update the current destination
                    distances[iteration][d] =  prev + w
        # return -1 if the Kth destination is not reachable, else return the shortest distance
        return -1 if distances[K+1][dst] == float("inf") else distances[K+1][dst]
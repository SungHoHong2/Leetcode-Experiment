class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        # create the bellman table that stores number of stops as rows and cities as columns
        bellman = [ [float('inf') for _ in range(n)] for _ in range(K+2)]
        # set the distances of the origin node to zero
        bellman[0][src] = 0
        # iterate K + 1 steps
        for i in range(1, K+2):
            # update all the cost from the previous step
            for u,v,w in flights:
                bellman[i][u] = bellman[i-1][u]
                bellman[i][v] = bellman[i-1][v]
            # update the new distances
            for u,v,w in flights:
                # update the minimum cost of the travel
                bellman[i][v] = min(bellman[i][v], bellman[i-1][u] + w)
        # return the minimum cost or -1 if the destination is not reachable within K + 1 steps
        return -1 if bellman[K+1][dst] == float('inf') else bellman[K+1][dst]
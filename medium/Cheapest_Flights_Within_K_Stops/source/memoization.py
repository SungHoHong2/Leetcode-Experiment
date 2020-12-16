class Solution:
    def findShortest(self, city, stops, dst, n):
        # return 0 if the destination is reached
        if city == dst:
            return 0
            # return inf if there are no more number of stops
        if stops == 0:
            return float('inf')
        # return the cache if the result of the cost is already cached
        if (city, stops) in self.cache:
            return self.cache[(city, stops)]
        # set a variable for recording the minimum cost
        cost = float('inf')
        # Iterate the weights of the neighbors
        for neigh in range(n):
            # if there is a neighbor according to the adjacency matrix
            if self.adjMatrix[city][neigh] > 0:
                # get the minimal cost created from traveling to the destination
                cost = min(cost, self.findShortest(neigh, stops - 1, dst, n) + self.adjMatrix[city][neigh])
        # cache the minimum cost
        self.cache[(city, stops)] = cost
        # return the minimum cost
        return self.cache[(city, stops)]

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        # set an adjacency matrix that uses weights as the value
        self.adjMatrix = [[0 for _ in range(n)] for _ in range(n)]
        for u, v, w in flights:
            self.adjMatrix[u][v] = w
            # set a cache
        self.cache = dict()
        # return the result from the recursion
        ans = self.findShortest(src, K + 1, dst, n)
        # return the result or -1 if the result is inf
        return ans if ans < float('inf') else -1
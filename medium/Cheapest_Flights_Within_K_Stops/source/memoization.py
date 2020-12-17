class Solution:
    def findShortest(self, city, stops, dst):
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
        ans = float('inf')
        # Iterate the weights of the neighbors
        for neigh, weight in self.flightMap[city]:
            # get the minimal cost created from traveling to the destination
            ans = min(ans, self.findShortest(neigh, stops - 1, dst) + weight)
        # cache the minimum cost
        self.cache[(city, stops)] = ans
        # return the minimum cost
        return self.cache[(city, stops)]

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        # create map using source as the key and the destination and the weight as the value
        self.flightMap = collections.defaultdict(list)
        for u, v, w in flights:
            self.flightMap[u].append((v,w))
        # set a cache
        self.cache = dict()
        # return the result from the recursion
        ans = self.findShortest(src, K + 1, dst)
        # return the result or -1 if the result is inf
        return ans if ans != float('inf') else -1
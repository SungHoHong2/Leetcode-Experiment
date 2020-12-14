class Solution:

    def findShortest(self, node, stops, dst, n):
        # return 0 if the destination is reached
        if node == dst:
            return 0
        # return inf if there are no more number of stops
        if stops < 0:
            return float("inf")
        # return the cache if the result of the cost is already cached
        if (node, stops) in self.memo:
            return self.memo[(node, stops)]
        # Iterate the weights of the neighbors
        ans = float("inf")
        for neighbor in range(n):
            # if there is a neighbor according to the adjacency matrix
            if self.adj_matrix[node][neighbor] > 0:
                # get the minimal cost created from traveling to the destination
                ans = min(ans, self.findShortest(neighbor, stops - 1, dst, n) + self.adj_matrix[node][neighbor])
        # cache the cost
        self.memo[(node, stops)] = ans
        # return the cost
        return ans

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        # set an adjacency matrix that uses weights as the value
        self.adj_matrix = [[0 for _ in range(n)] for _ in range(n)]
        for s, d, w in flights:
            self.adj_matrix[s][d] = w
        # set a cache
        self.memo = {}
        # return the result from the recursion
        result = self.findShortest(src, K, dst, n)
        # return the result or -1 if the result is inf
        return -1 if result == float("inf") else result
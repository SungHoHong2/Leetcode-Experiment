class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # set up the map that uses the origin as the key and the list of destinations as the value
        self.flightMap = collections.defaultdict(list)
        # iterate the tickets
        for ticket in tickets:
            # store the key as the origin and the destination as the value to the map
            self.flightMap[ticket[0]].append(ticket[1])
        # sort the destination according to the lexical descending order
        for src in self.flightMap:
            self.flightMap[src].sort(reverse=True)
        # start the depth-first search from JFK
        return reversed(self.dfs('JFK'))

    def dfs(self, src):
        """
        post-order dfs:
        start accumulating the destinations at the finishing point of the dfs
        """
        # set the returning array
        ans = list()
        # explore and collect destinations using dfs
        while self.flightMap[src]:
            ans += self.dfs(self.flightMap[src].pop())
        # add the source to the returning array
        ans.append(src)
        # return the destinations
        return ans
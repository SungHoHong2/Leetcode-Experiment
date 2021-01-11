class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # set up the map that uses the origin as the key and the list of destinations as the value
        flightMap = collections.defaultdict(list)
        # iterate the tickets
        for ticket in tickets:
            # store the key as the origin and the destination as the value to the map
            flightMap[ticket[0]].append(ticket[1])
        # sort the destination according to the lexical descending order
        for src in flightMap:
            flightMap[src].sort(reverse=True)
        # start the depth-first search from JFK
        return reversed(self.dfs('JFK', flightMap))

    def dfs(self, src, flightMap):
        """
        post-order dfs:
        start accumulating the destinations at the finishing point of the dfs
        """
        # set the returning array
        ans = list()
        # deplete and collect destinations using dfs
        while flightMap[src]:
            ans += self.dfs(flightMap[src].pop(), flightMap)
        # add the source to the returning array
        ans.append(src)
        # return the destinations
        return ans
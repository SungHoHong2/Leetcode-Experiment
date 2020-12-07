class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # set up the map that uses the origin as the key and the list of destinations as the value
        self.flightMap = collections.defaultdict(list)
        # iterate the tickets
        for ticket in tickets:
            # store the key as the origin and the destination as the value to the map
            self.flightMap[ticket[0]].append(ticket[1])
        # sort the destination according to the lexical descending order
        for key in self.flightMap:
            # Note that we could have multiple identical flights, i.e. same origin and destination.
            self.flightMap[key].sort(reverse=True)
        # start the depth-first search from JFK
        return self.dfs('JFK')[::-1]

    def dfs(self, origin):
        ans = []
        # get the destination list
        destinations = self.flightMap[origin]
        # explore the destinations of the origin
        while destinations:
            ans.extend(self.dfs(destinations.pop()))
        # append the origin to the array
        ans.append(origin)
        # return the array
        return ans

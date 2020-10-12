class Solution(object):
    def findItinerary(self, tickets):
        # set up the map that uses the origin as the key and the list of destinations as the value
        self.flightMap = collections.defaultdict(list)
        # iterate the tickets
        for ticket in tickets:
            # store the key as the origin and the destination as the value to the map
            origin, dest = ticket[0], ticket[1]
            self.flightMap[origin].append(dest)
        # sort the destination according to the lexical descending order
        for origin, itinerary in self.flightMap.items():
            # Note that we could have multiple identical flights, i.e. same origin and destination.
            itinerary.sort(reverse=True)
        # set up the return array
        self.result = []
        # start the depth-first search from JFK
        self.DFS('JFK')
        # reconstruct the route backwards
        return self.result[::-1]

    def DFS(self, origin):
        # get the destination list
        destList = self.flightMap[origin]
        # loop until the destination list is depleted
        while destList:
            # pop the descending order of destination
            nextDest = destList.pop()
            # invoke the dfs recursion
            self.DFS(nextDest)
        # append the origin to the array
        self.result.append(origin)

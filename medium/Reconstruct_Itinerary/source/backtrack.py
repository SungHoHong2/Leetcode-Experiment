class Solution(object):
    def findItinerary(self, tickets):
        # set a map that stores the desintations of the flight tickets
        self.flightMap = collections.defaultdict(list)
        # iterate the tickets
        for ticket in tickets:
            # store the key as the origin and the append the possible destinations
            origin, dest = ticket[0], ticket[1]
            self.flightMap[origin].append(dest)
        # set a map that tracks the visited flights
        self.visited = {}
        # sort the desintations in a lexical order and set the visited flights
        for origin, itinerary in self.flightMap.items():
            # sort the destinations according to the lexical order
            itinerary.sort()
            # append the visited map with the list of unvisited flights
            self.visited[origin] = [False] * len(itinerary)
        # get the total number of ticket
        self.flights = len(tickets)
        # initialize the starting route with JFK
        route = ['JFK']
        # return the possible route from backtracking
        return self.backtracking('JFK', route)

    def backtracking(self, origin, route):
        # return the route if the recursion found the full path
        if len(route) == self.flights + 1:
            return route
        # iterate the destinations from the current flight
        for i, nextDest in enumerate(self.flightMap[origin]):
            # if the destination is not a visited flight
            if not self.visited[origin][i]:
                # mark the destination flight as visited
                self.visited[origin][i] = True
                # invoke the recursion with the next destination
                ans = self.backtracking(nextDest, route + [nextDest])
                self.visited[origin][i] = False
                # return the route if the recursion found a full path
                if len(ans) == self.flights + 1:
                    return ans
        # return the empty list if the full path is not found
        return list()

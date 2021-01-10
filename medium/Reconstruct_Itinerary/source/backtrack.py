class Solution(object):
    def findItinerary(self, tickets):
        # set a map that stores flight as the key and the destinations as the value
        self.flightMap = collections.defaultdict(list)
        # iterate the tickets
        for ticket in tickets:
            # store the key as the origin and the append the possible destinations
            src, dest = ticket
            self.flightMap[src].append(dest)
        # set a map that tracks the visited flights
        self.visited = dict()
        # sort the destinations in a lexical order and set the visited flights
        for src, dests in self.flightMap.items():
            # sort the destinations according to the lexical order
            dests.sort()
            # append the visited map with the list of unvisited flights
            self.visited[src] = [0 for _ in dests]
        # set the total number of airports that needs to be included in the route == JFK + dests
        self.flights = len(tickets) + 1
        # initialize the starting route with JFK
        route = ['JFK']
        # return the complete route from backtracking
        return self.backtracking('JFK', route)

    def backtracking(self, src, route):
        # return the route if the all the airports are included in the route
        if len(route) == self.flights:
            return route
        # iterate the destinations from the current flight
        for i, dest in enumerate(self.flightMap[src]):
            # if the destination is not a visited flight
            if not self.visited[src][i]:
                # update the destination flight as visited
                self.visited[src][i] = True
                # invoke the recursion with the next destination
                ans = self.backtracking(dest, route + [dest])
                # reset the destination flight
                self.visited[src][i] = False
                # return the route if all the airports are included in the route
                if len(ans) == self.flights:
                    return ans
        # return the empty list if no complete route is found
        return list()
class Solution(object):

    def findItinerary(self, tickets):
        # set a map that uses a value as a list
        self.flightMap = collections.defaultdict(list)
        # iterate the tickets
        for ticket in tickets:
            # store the key as the origin and the append the possible destinations
            origin, dest = ticket[0], ticket[1]
            self.flightMap[origin].append(dest)
        # set a map that tracks the visited flights
        self.visitBitmap = {}
        for origin, itinerary in self.flightMap.items():
            # sort the destinations according to the lexical order
            itinerary.sort()
            # append the visited map with the list of unvisited flights
            self.visitBitmap[origin] = [False]*len(itinerary)
        # get the total number of ticket
        self.flights = len(tickets)
        # set up the return list
        self.result = []
        # initialize the starting route with JFK
        route = ['JFK']
        # start the recursion
        self.backtracking('JFK', route)
        # return the result
        return self.result

    def backtracking(self, origin, route):
        # if the recursion found the full travel path
        if len(route) == self.flights + 1:
            # store the route to the result
            self.result = route
            # return true
            return True
        # iterate the destinations from the current flight
        for i, nextDest in enumerate(self.flightMap[origin]):
            # if the destination is not a visited flight
            if not self.visitBitmap[origin][i]:
                # mark the destination flight as visited
                self.visitBitmap[origin][i] = True
                # invoke the recursion with the next destination
                ret = self.backtracking(nextDest, route + [nextDest])
                self.visitBitmap[origin][i] = False
                # if the recursion found a full path
                if ret:
                    # return true
                    return True
        # if the full path is not found return false
        return False
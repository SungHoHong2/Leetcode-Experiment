from collections import defaultdict


class Solution(object):

    def findItinerary(self, tickets):

        # build a graph data structure from the given input.
        # graph identify a list of potential destinations, given an origin.
        # <origin, [destinations]>.
        self.flightMap = defaultdict(list)
        for ticket in tickets:
            origin, dest = ticket[0], ticket[1]
            self.flightMap[origin].append(dest)

        # create visit map
        self.visitBitmap = {}
        # order the destination list for each entry in lexical order.
        for origin, itinerary in self.flightMap.items():
            # sort the destinations with lexical order
            itinerary.sort()
            # add the status of visits
            self.visitBitmap[origin] = [False] * len(itinerary)

        # count total number of available flights
        self.flights = len(tickets)

        # return result
        self.result = []

        # start backtracking
        route = ['JFK']
        self.backtracking('JFK', route)
        return self.result

    def backtracking(self, origin, route):

        # if the total route is same as the total length of the tickets
        # self.flights = len(tickets)
        if len(route) == self.flights + 1:
            self.result = route
            return True

        for i, nextDest in enumerate(self.flightMap[origin]):
            print(i, nextDest)
            if not self.visitBitmap[origin][i]:
                # mark the visit before the next recursion
                self.visitBitmap[origin][i] = True
                ret = self.backtracking(nextDest, route + [nextDest])
                self.visitBitmap[origin][i] = False

                # end the search if the backtracking successfully got all the results
                if ret:
                    return True

        return False
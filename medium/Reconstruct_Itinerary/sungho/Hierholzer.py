from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        # create a dictionary that holds list
        self.visitMap = defaultdict(list)

        # iterate through the ticket
        for ticket in tickets:
            # map the dictionary with the origin, destiation
            origin, destination = ticket[0], ticket[1]
            self.visitMap[origin].append(destination)

        # sort the itinerary
        for org, dest in self.visitMap.items():
            dest.sort(reverse=True)

        # initiate the result list
        self.result = []

        # start the DFS
        self.DFS('JFK')

        return self.result[::-1]

    def DFS(self, origin):

        # get the destination list
        destList = self.visitMap[origin]

        # iterate through destination list
        while destList:
            # get the destination item by popping
            dest = destList.pop()
            # recursively enter the DFS function
            self.DFS(dest)

        # append the result
        self.result.append(origin)

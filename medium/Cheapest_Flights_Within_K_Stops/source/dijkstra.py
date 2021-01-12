from heapq import heappush,heappop

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        # create map using source as the key and the destination and the weight as the value
        graph = collections.defaultdict(list)
        for u, v, w in flights:
            graph[u].append((w,v))
        # create a priority queue
        pq = list()
        # append information of the starting point (price, stops, city) to the heap
        heappush(pq, (0, K+1, src))
        # loop until the heap depletes
        while pq:
            # get the information of the city that accumulated the cheapest price
            price, stops, city = heappop(pq)
            # return the price if the current city is the destination
            if city == dst:
                return price
            # if there are still number of stops left
            if stops > 0:
                # iterate the neighbors of the current city
                for dest_price, dest in graph[city]:
                    # append the next city to the heap
                    heappush(pq, (price+dest_price, stops-1, dest))
        # return -1 if nothing is found
        return -1
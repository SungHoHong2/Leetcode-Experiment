import heapq
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        # create a map that treats list as a value
        graph = collections.defaultdict(list)
        # create a priority queue
        pq = []
        # store map using source as the key and the destination and the weight as the value
        for u, v, w in flights:
            graph[u].append((w, v))
        # append information of the starting point (price, stops, city) to the heap
        heapq.heappush(pq, (0, K+1, src))
        # loop until the heap depletes
        while pq:
            # get the information of the current city from the heap
            price, stops, city = heapq.heappop(pq)
            # return the price if the current city is the destiation
            if city is dst: return price
            # if there are still number of stops left
            if stops>0:
                # iterate the neighbors of the current city
                for price_to_nei, nei in graph[city]:
                    # append the next city to the heap
                    heapq.heappush(pq, (price+price_to_nei, stops-1, nei))
        # return -1 if nothing is found
        return -1
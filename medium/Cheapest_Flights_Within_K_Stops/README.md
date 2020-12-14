### Cheapest Flights Within K Stops
**Dijkstra's Algorithm**
- Concepts 
- [Source code]()
```python
import heapq
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        # create a map that treats list as a value 
        # create a priority queue
        # store map using source as the key and the destination and the weight as the value      
        # append information of the starting point (price, stops, city) to the heap 
        # loop until the heap depletes 
            # get the information of the current city from the heap
            # return the price if the current city is the destiation 
            # if there are still number of stops left
                # iterate the neighbors of the current city 
                    # append the next city to the heap
        # return -1 if nothing is found
        pass
```

**Depth-First-Search with Memoization**
- Concepts 
    - `recursion(neighbor, stops + 1) + weight(node, neighbor)`
- [Source code]()
```python
class Solution:
    def findShortest(self, node, stops, dst, n):
        # return 0 if the destination is reached    
        # return inf if there are no more number of stops 
        # return the cache if the result of the cost is already cached
        # Iterate the weights of the neighbors 
            # if there is a neighbor according to the adjacency matrix 
                # get the minimal cost created from traveling to the destination
        # cache the cost 
        # return the cost 
        pass
    
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        # set an adjacency matrix that uses weights as the value 
        # set a cache 
        # return the result from the recursion
        # return the result or -1 if the result is inf 
        pass
```

**Bellman-Ford**
- [Original version](source/BellmanV1.py)
- [Space optimized version](source/BellmanV2.py)
```python
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        # create two arrays for storing distances and swapping 
        # set the distnace of the origin node to zero
        # K + 1 iterations of Bellman Ford
            # Iterate K times 
                # even number & 1  = 0, odd number & 1 = 1 
                # get the total distance of the "origin" from the previous array  
                # get the total distance of the destination from the current array  
                # if the newly added weight 
                    # update the current destination 
        # return -1 if the Kth destination is not reachable, else return the shortest distance
        pass 
```

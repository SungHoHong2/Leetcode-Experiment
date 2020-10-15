### Cheapest Flights Within K Stops
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

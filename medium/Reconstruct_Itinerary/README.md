### Reconstruct Itinerary
**Backtracking + Greedy**
- Concept 
    - `Backtracking` is used to enumerate all possible solutions for a problem, in a trial-fail-and-fallback strategy.
    - `Greedy algorithm` is used at each step we would pick the destination `greedily` in lexical order
- Time Complexity `O(E^d)`
    - `E` is the number of total flights
    - `d` is the number of flights from an airport
- Space Complexity `O(V+E)`
    - `V` is the number of airports 
    - `E` is the number of flights 
- [Source code](source/backtrack.py)

```python
class Solution(object):
    def findItinerary(self, tickets):
        # set a map that stores flight as the key and the destinations as the value
        # iterate the tickets
            # store the key as the origin and the append the possible destinations
        # set a map that tracks the visited flights
        # sort the destinations in a lexical order and set the visited flights
            # sort the destinations according to the lexical order
            # append the visited map with the list of unvisited flights
        # set the total number of airports that needs to be included in the route == tickets + 1 
        # initialize the starting route with JFK
        # return the complete route from backtracking
        pass

    def backtrack(self, route):
        # get the current destination 
        # return the route if the all the airports are included in the route
        # iterate the destinations from the current flight
            # if the destination is not a visited flight
                # update the destination flight as visited
                # invoke the recursion with the next destination
                # reset the destination flight
                # return the route if all the airports are included in the route
        # return the empty list if no complete route is found 
        pass
```

**Post Order DFS**
- Concept
    - Suppose each input is guaranteed to have a solution
    - Collect the destination of the flight backwards 
        - Reverse the lexical order since the answer is collected in `post order` 
    - Follow `post Order` because the `dfs` may find the incomplete destination  before finding complete destination
        - `Post order` allows the dfs to collect the order that connects the flight in a complete destination  
- Time Complexity `O(E * Elog(E))`
    - `E`: The DFS traverses each edge once
    - `NlogN`: need to sort the outgoing edges for each vertex.
        - In the worst case where the graph is not balanced, i.e. the connections are centered in a single airport.
- Space Complexity `O(V+E)`
    - `V` is the number of airports 
    - `E` is the number of flights 
- [Source code](source/dfs.py)

```python
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # set up the map that uses the origin as the key and the list of destinations as the value
        # iterate the tickets
            # store the key as the origin and the destination as the value to the map
        # sort the destination according to the lexical descending order
        # start the depth-first search from JFK
        pass

    def dfs(self, src, flightMap):
        """
        post-order dfs: 
        start accumulating the destinations at the finishing point of the dfs
        """
        # set the returning array
        # deplete and collect destinations using dfs
        # add the source to the returning array
        # return the destinations
        pass
```
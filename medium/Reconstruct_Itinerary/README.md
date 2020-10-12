### Reconstruct Itinerary
**Backtracking + Greedy**
- `Backtracking` is used to enumerate all possible solutions for a problem, in a trial-fail-and-fallback strategy.
- `Greedy algorithm` is used at each step we would pick the destination `greedily` in lexical order
- [Source code](source/)

```python
class Solution(object):
    def findItinerary(self, tickets):
        # set a map that uses a value as a list
        # iterate the tickets
            # store the key as the origin and the append the possible destinations
        # set a map that tracks the visited flights
        # iterate the map that stores all possible destinations
            # sort the destinations according to the lexical order
            # append the visited map with the list of unvisited flights
        # get the total number of ticket
        # set up the return list
        # initialize the starting route with JFK
        # start the recursion
        # return the result
        pass 

    def backtracking(self, origin, route):
        # if the recursion found the full travel path
            # store the route to the result
            # return true
        # iterate the destinations from the current flight
            # if the destination is not a visited flight
                # mark the destination flight as visited
                # invoke the recursion with the next destination
                # if the recursion found a full path
                    # return true
        # if the full path is not found return false
        pass
```


**Hierholzer's Algorithm**
- In graph theory, an `Eulerian trail` is a trail in a finite graph that visits every edge exactly once (allowing for revisiting vertices).
- `Hierholzer's algorithm` is the stepwise construction of the Eulerian cycle by connecting disjunctive circles.
    - It starts with a random node and then follows an arbitrary unvisited edge to a neighbor. 
    - This step is repeated until one returns to the starting node. This yields a first circle in the graph.
    - If this circle covers all nodes it is an Eulerian cycle and the algorithm is finished. Otherwise, one chooses another node among the cycles' nodes with unvisited edges and constructs another circle, called subtour.
- [Source code](source/)

```python
class Solution(object):
    def findItinerary(self, tickets):
        # set up the map that uses the origin as the key and the list of destinations as the value
        # iterate the tickets
            # store the key as the origin and the destination as the value to the map
        # sort the destination according to the lexical descending order
            # Note that we could have multiple identical flights, i.e. same origin and destination.
        # set up the return array
        # start the depth-first search from JFK
        # reconstruct the route backwards
        pass 

    def DFS(self, origin):
        # get the destination list
        # loop until the destination list is depleted
            # pop the descending order of destination
            # invoke the dfs recursion
        # append the origin to the array
        pass 
```
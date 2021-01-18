### Critical Connections in a Network
**Tarjan's bridge-finding algorithm**
- [Concepts](images/tarjan.png)
- [Source code](source/tarjan.py)
- [Reference #1](https://www.youtube.com/watch?v=jFZsDDB0-vo)
- [Reference #2](https://www.youtube.com/watch?v=RYaakWv5m6o)

```python
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # set the hashmap for storing the list of undirected src and dests
        # set the pointer for tracking the order of discovery
        # set the hashmap to record the minimum rank that the nodes can reach      
        # set the table to mark the visited nodes 
        # build an undirected graph 
        # set the list for returning the critical edges
        # set the pointer for the previous vertex
        # set the pointer for the current vertex
        # start the dfs
        # return the critical edges 
        pass
        
    def dfs(self, res, rank, prev, current):
        # mark the node as visited 
        # set the minimum rank
        # explore the neighbors 
            # if the vertex is not visited
                # explore the neighbors with dfs 
            # if the node did not reach the deadend
                # update the lowest rank reachable once formed a cycle
                # append the critical edge if the edge does not return as a cycle
        pass
```

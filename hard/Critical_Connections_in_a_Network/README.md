### Critical Connections in a Network
**Tarjan's bridge-finding algorithm**
- [Concepts](images/tarjan.png)
- [Source code](source/tarjan.py)
- [Reference #1](https://www.youtube.com/watch?v=jFZsDDB0-vo)
- [Reference #2](https://www.youtube.com/watch?v=RYaakWv5m6o)

```python
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # set the hashmap to build an undirected graph
        # set the hashmap to record the minimum rank that the nodes can reach      
        # set the hashset to mark the visited nodes 
        # return the critical edges from the dfs (rank, prev, src)
        pass
        
    def dfs(self, rank, prev, src):
        # set the list for returning the critical edges
        # mark the node as visited
        # set the minimum rank
        # explore the neighbors 
            # if the vertex is not visited
                # combine the returning edges by exploring the neighbors with dfs 
            # if the node did not reach the dead end
                # update the lowest rank reachable once formed a cycle
                # append the edge as the critical if the edge does not return as a cycle
        # return the critical edges 
        pass
```
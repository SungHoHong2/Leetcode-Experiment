### Number of Provinces
**DFS**
- [Source code](source/DFS.py)
```python
class Solution:
    def dfs(self, i):
        # return if province is out of range or already visited
        # mark the province as visited
        # iterate the neighbors
            # if the neighbors are connected
                # run the dfs
        pass

    def findCircleNum(self, adjacency: List[List[int]]) -> int:
        # set a adjacency table as global
        # set the visited table
        # set the total number of provinces
        # iterate the provinces
            # if the province is not visited
                # increase the number of province
                # run the dfs
        # return the total number of provinces
        pass
```

**BFS**
- [Source code](source/BFS.py)
```python
class Solution:
    def findCircleNum(self, adjacency: List[List[int]]) -> int:
        # set the total number of provinces 
        # set a hashset that stores the unvisited provinces
        # set the queue for BFS
        # loop until all the unvisited provinces are explored 
            # pop and append one of the unvisited provinces to the queue 
            # increase the number of province 
            # loop until the queue is empty 
                # pop a province from the queue 
                # iterate its neighbors 
                    # if the neighbor is connected and unvisited 
                        # append the neighbor to the queue 
                        # remove the neighbor from the unvisited provinces
        # return the total number of provinces
        pass
```

**Solution3**
- [Concepts](images/)
- [Source code](source/)
- [Reference #1]()
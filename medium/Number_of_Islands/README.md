### Number of Islands

**Depth First Search**
- [Source code](source/dfs.py)

```python
class Solution:
    def dfs(self, grid, r, c):
        # skip if the table is viewed, water, or out of range
        # mark index as viewed
        # search through all the table recursively
    def numIslands(self, grid: List[List[str]]) -> int:
        # if the grid has nothing return 0
        # set variable for the total number of islands 
        # iterate the cells of the table
                # if there is a ground
                    # add one island
                    # execute the recursive depth-first-search
        # return the total number of islands 
```

**Breadth First Search**
- [Source code](source/bfs.py)
```python
class Solution:
    def numIslands(self, grid):
        # if there is not grid return 0
        # set variable for the total number of islands
        # create a set that contains the address of the cells containig value "1"
        # iterate the set until the set is empty
            # increase the number of total islands
            # init a queue
            # pop one island from the set to the queue
            # iterate until the queue is empty
                # pop one island from the queue
                # empty the neighbors of the (row,col) that are in the set
                    # if the neighbors are part of the set
                        # remove the neighbor from the set
                        # add the neighhbor to the queue
        # return the final result
```

**Disjoint Set**
- [Source code](source/disjoint.py)



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

**Disjoint Set**
- [Source code](source/disjoint.py)



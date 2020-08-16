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
        # loop the set until the set is empty
            # increase the number of total islands
            # init a queue
            # pop one island from the set to the queue
            # loop until the queue is empty
                # pop one island from the queue
                # empty the neighbors of the (row,col) that are in the set
                    # if the neighbors are part of the set
                        # remove the neighbor from the set
                        # add the neighhbor to the queue
        # return the final result
```

**Disjoint Set**
- [Source code](source/disjoint.py)

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # if grid is not valid
        # get the length of the row and the col of the grid
        # set the parent table where all items themselves are the parents
        # set the ranking table for the parents
        # set parent of the cell
        def setParent(curr, parent):
            # get the address of the current cell
            # store the parent address to the current cell
        # return the rank of the parent
        def getRank(parent):
            # get the address of the parent
            # return the rank from the table
        # update the rank of the parent
        def setRank(parent, rank):
            # get the address of the parent
            # update the rank
        # find the parent of the node
        def find(current):
            # get the index of the node
            # set the temporary pointer just in case the current node already has a parent
            # if the selected node already has a parent
                # get the address of the parent
            # update the parent table of that node
            # return the index of the parent
        # merge two groups together
        def union(a, b):
            # get the parents of both 'a' and 'b'
            # return the ranks of the parents of both 'a' and 'b'
            # if the rank of the 'b' is higher
                # set the parent of 'a' to parent of 'b'
            # if the rank of the 'a' is higher
                # set the parent of 'b' to parent of 'a'
            # if the ranks of 'a' and 'b' are the same
                # increase the number of rank and merge the group
        # iterate the grid
                # if the cell is the ground
                    # get the right and bottom cells
                        # merge all the (row,col) that contains "1"
        # initialize the total number of islands
        # iterate the grid
                # if it is a ground and is the parent
                    # increase the number of islands
        # return the number of islands
```

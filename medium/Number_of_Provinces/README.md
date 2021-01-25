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

**Union-Find**
- [Source code](source/disjoint.py)
```python
class Solution:
    def findCircleNum(self, adjacency: List[List[int]]) -> int:
        # set the table of parents for the disjoint set
        # set the table of ranking for the disjoint set
        
        def getParent(i):
            # set the temporary pointer just in case the current node already has a parent
            # if the selected node already has a parent
                # get the address of the parent
                # update the parent table of that node
            # return the index of the parent
            pass
        
        def setParent(curr, parent):
            # store the parent address to the current cell
            pass
        
        def getRank(parent):
            # return the rank from the table
            pass
        
        def setRank(parent, rank):
            # update the rank
            pass
        
        def union(a, b):
            # get the parents of both 'a' and 'b'
            # return the ranks of both 'a' and 'b'
            # if the rank of the 'b' is higher
                # set the parent of 'a' to parent of 'b'
            # if the rank of the 'a' is higher
                # set the parent of 'b' to parent of 'a'
            # if the ranks of 'a' and 'b' are the same
                # increase the number of rank and merge the group
            pass

        # iterate the number of nodes 
            # iterate the neighbors 
                # if the neighbor is valid 
                    # merge two provinces
            
        # count the number of provinces that has the parent as itself
        # return the total number of provinces
        pass
```

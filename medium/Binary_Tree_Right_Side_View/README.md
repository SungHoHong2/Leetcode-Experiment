### Binary Tree Right Side View

**BFS: Two Queues**
- [concepts](images/two_queues.png)
- [source code](source/two_queues.py)
```python
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        # set the list that keep record of the right side element 
        # return empty list if there is no input 
        # create the FIFO queue for each level 
        # explore the tree to the last level 
            # get the current level  
            # create a new FIFO queue for the next level
            # explore the nodes in the current level 
                # pop out the nodes from the left 
                # add the child nodes for the next_level array
            # the rightmost node in each level is the rightside of the tree
        # return the list of nodes that are from the rightside
        pass
```

**BFS: One Queue + Sentinel**
- [source code](source/sentinel.py)
```python
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        # set the return value
        # return the empty list if there is no input
        # create the first level with the sentinel
        # set a variable to track the rightmost nodes
        # explore the nodes in each level
            # assign the previous node and the next node
            # add child nodes for the next level
                # stop until the current node reaches "None" (end of the level)
            # append the rightmost node to the return list
            # add a sentinel if there is a next level or let the queue be empty
        # return the list of the rightside nodes
        pass
```
 
**BFS: One Queue + Level Size Measurements**
- [source code](source/level_size.py)
```python
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        # set the return value
        # return the empty list if there is no input
        # create the first level
        # explore the levels in the tree
            # get the length of the current level
            # explore the nodes in the current level
                # pop the node of the level from the left
                # append to the return list if the current node is the rightmost element
                # add child nodes in the queue
        # return the list of nodes from the rightside
        pass
```

**Recursive DFS**
- [source code](source/dfs.py)
```python
class Solution:
    def dfs(self, node, level):
        # current level matches with the number of returning nodes
            # append the node to the return list
        # explore the right node as the priority
        pass

    def rightSideView(self, root: TreeNode) -> List[int]:
        # set the return value
        # return the empty list if there is no input
        # invoke the dfs recursion
        # return the list of the nodes from the rightside
        pass
```    

### Serialize and Deserialize Binary Tree
**DFS**
- [Source code](source/DFS.py)
```python
class Codec:
    def serialize(self, root):
        def dfs(node, string):
            # append the string with "None," when the node is blank
            # append the value to the return string
            # append the value from the left child
            # append the value from the right child
            # return the string
            pass
        # return the string from the dfs
        pass

    def deserialize(self, data):
        def dfs(queue):
            # if the current item is None
                # pop the current item
                # return None
            # create the node with the current item
            # create the left child
            # create the right child
            # return the node
            pass 
        # return the reconstructed tree from deserialization
        pass
```

**BFS**
- [Source code](source/BFS.py)
```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        # return empty string if the input is invalid
        # set the double-ended queue  
        # append the root to the queue 
        # set the return string 
        # loop the queue until it is depleted 
            # pop item from the left side of the queue 
            # append 'None,' to the return string and continue if the node is None
            # append the node value to the return string 
            # append the left child to the queue 
            # append the right child to the queue 
        # return the string 
        pass

    def deserialize(self, data):
        # return None if the data is invalid 
        # convert the string to an array with ','
        # create the root node 
        # create the double-ended queue
        # append the root to the queue 
        # set the index for the input array
        # loop until the queue or input array is depleted
            # pop the queue from the left
            # create the left child node if the item of the array is valid 
            # create the right child node if the item of the array is valid 
        # return the head of the tree
        pass
```
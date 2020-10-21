### Flatten a Multilevel Doubly Linked List

**DFS by Recursion**
- [source code](source/recursive.py)
```python
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        # return none if there is no input
        # create a fake head
        # run the recursion (prev, next)
        # detach the pseudo head from the real head
        # return the real head
        pass

    def flatten_dfs(self, prev, curr):
        # return the tail if the recursion reached its leaf
        # connect the previous and the current node
        # get the pointer to the right node
        # connect the current node with its children by using recursion
        # remove the child node of the current node
        # connect the last child with the right node by using recursion
        pass 
```

**DFS by Iteration**
- [concepts](images/iterative.png)
- [source code](source/iterative.py)
```python
class Solution(object):
    def flatten(self, head):
        # return nothing if there is no input
        # create a fake head
        # assign the fake head the prev
        # generate a stack
        # append the real head
        # iterate through the stack
            # pop the latest inserted node
            # connect the previous and the current node
            # push the next node into the stack
            # push the child node into the stack
                # remove the child pointer of the current node
            # set the current node as the previous node
        # detach the pseudo head node from the result.
        # return the flattened list
        pass 
```
### Copy List with Random Pointer
**Recursive**
- [Source code](source/)
```python
class Solution:
    def __init__(self):
        # initialize a cache
    def copyRandomList(self, head: 'Node') -> 'Node':
        # if the node is null
            # return none
        # if the node is in the cache
            # return the cached node
        # create a node
        # add the node to the cache
        # receive the recursive function from the next
        # receive the recursive function from the random
        # return the node
```

**~~Iterative with~~ O(N) Space**
- [Source code](source/)
```python
class Solution(object):
    def __init__(self):
        # create a cache
    # get cloned node function
    def getClonedNode(self, node):
        # if the node is NULL
            # return None
        # if the node is in the cache
            # return the node from the cache
        # save the node in the cache
        # return the node
    def copyRandomList(self, head):
        # if the node is NULL
            # return None
        # save the header for the original linked-list
        # create a header for the new linked-list
        # save the pointer to return the header of the new linked-list
        # loop until the original node is depleted
            # create the node from the random pointer
            # create the node from the next pointer
            # move the previous linked-list forward
            # move the new linked-list forward
        # return the header of the new linked-list
```

**Iterative with O(1) Space**
- [Source code](source/)
```python
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        # if the node is Null
            # return None
        # set the current pointer to the head
        # loop until the Linked-list is depleted
            # create a new node
            # interweave the new node
            # move the current pointer forward
        # set the current pointer to the head
        # loop until the Linked-list is depleted
            # if the node has a random pointer
                # add the random pointer to the new node
            # if there is no random pointer
                # mark the random pointer to None
            # connect the new node with the new node
        # set the current pointer
        # loop until the new Linked-list is depleted
            # connect the only nodes from the new linked-list
        # return the new Linked-list
```
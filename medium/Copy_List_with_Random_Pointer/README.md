### Copy List with Random Pointer
**Recursive**
- Intuition
    1. Declare a global cache that stores the pointers of the node
    1. Explore from root to leaf and add all the nodes in cache 
    1. Return from leaf to root and use the cache to set the random pointers 
- [Source code](source/Recursive.py)
```python
class Solution:
    def __init__(self):
        # initialize a cache
        pass
    def copyRandomList(self, head: 'Node') -> 'Node':
        # return none if the node is null
        # return the cached node if the node is in the cache
        # create a node
        # add the node to the cache
        # receive the recursive function from the next
        # receive the recursive function from the random
        # return the node
        pass
```

**Iteration with O(N) Space**
- Intuition
    1. Declare a cache that stores the pointers of the node
    2. Explore the linked-list while storing the nodes in cache and creating the new linked-list

- [Source code](source/Iteration.py)
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

**Iteration with O(1) Space**
- Intuition
    - Avoid using `hashtable` to store the pointers 
    1. Store the new items next to the old items in the linked list 
    2. Find the nodes for random pointers by looking into the old items (items.next)
    3. Remove the old items in the linked list    
- [Source code](source/Iteration2.py)
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
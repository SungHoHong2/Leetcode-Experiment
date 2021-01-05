### Copy List with Random Pointer
**Recursive**
- Concepts
    1. Declare a global cache that stores the pointers of the node
    1. Explore from root to leaf and add all the nodes in cache 
    1. Return from leaf to root and use the cache to set the random pointers 
    - Time Complexity
        - `O(n)` : the number of nodes in the linked list
    - Space Complexity 
        - `O(n)` : the recursion stack and the hashmap 
- [Source code](source/Recursive.py)
```python
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
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
- Concepts
    1. Declare a cache that stores the pointers of the node
    2. Explore the linked-list while storing the nodes in cache and creating the new linked-list
    - Time Complexity
        - `O(n)` : the number of nodes in the linked list
    - Space Complexity 
        - `O(n)` : the recursion stack and the hashmap 
- [Source code](source/Iteration.py)
```python
class Solution(object):
    def __init__(self):
        # create a cache
        pass
    # get cloned node function
    def getClonedNode(self, node):
        # return None if the node is NULL
        # return the cache if the node is in the cache
        # save the node in the cache
        # return the node
        pass
    
    def copyRandomList(self, head):
        # return None if the node is NULL
        # save the header for the original linked-list
        # create a header for the new linked-list
        # save the pointer to return the header of the new linked-list
        # loop until the original node is depleted
            # create the node from the random pointer
            # create the node from the next pointer
            # move the previous linked-list forward
            # move the new linked-list forward
        # return the header of the new linked-list
        pass
```

**Iteration with O(1) Space**
- Concepts
    - Avoid using `hashtable` to store the pointers 
    1. Store the new items next to the old items in the linked list 
    2. Find the nodes for random pointers by looking into the old items (items.next)
    3. Remove the old items in the linked list    
    - Time Complexity
        - `O(n)` : the number of nodes in the linked list
    - Space Complexity 
        - `O(1)` : does not create new linked list     
    
- [Source code](source/Iteration2.py)
```python
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        # return None if the node is Null
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
        pass
```
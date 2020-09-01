### LRU Cache

**Ordered dictionary**
- [Source code](source/OrderedDict.py)

```python
class LRUCache():
    def __init__(self, capacity: int):
        # create collections.OrderedDict which is a combination of hashmap and linked-list
        # indicator of the total size of the LRU
    def get(self, key):
        # if there is no key
            # return -1
        # set the item to most recently checked
        # return the result from the hashmap
    def put(self, key, value):
        # if the key exists
            # set the item to most recently checked
        # update the. value
        # if the total capacity of the LRU is full remove the least recently checked
```

**HashMap + LinkedList**
- [Source code](source/DoubleLink.py)
```python
# strucutre for double-linked node
class DLinkedNode():
    def __init__(self):
        # set the variable for the key (int)
        # set the variable for the value (int)
        # set the prev pointer
        # set the next pointer
class LRUCache():
    def __init__(self, capacity: int):
        # set the hashmap for cache
        # set the variable for capacity
        # create a head and tail pointer
        # connect the head with the tail
        # connect the tail with the head
    def get(self, key):
        # if the key does not exist in the cache
            # return -1
        # update the key as the most recently viewed
        # return the value of the key
    # function for updating the item as the most recently viewed
    def move_to_head(self, node):
        # remove the current item
        # add the new item
    # function for removing the item
    def remove_node(self, node):
        # get the neightbors of the current item
        # remove the current item by connecting the neighbors
    # function for adding a new item
    def add_node(self, node):
        # update the pointers of the new item
        # update the pointers of the neighbors 
    def put(self, key, value):
        # if the key is not part of the cache
            # create a new item
            # add in the dictionary
            # add in the double linked node
            # if the size of the cache exceeds the capacity remove the least accessed node
                # get the key of the least recently viewed item
                # remove the key from the node
                # delete the key from the cache
        # if the key is part of the cache
            # update the cache
            # update the item as the most recently viewed
```

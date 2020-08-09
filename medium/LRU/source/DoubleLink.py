# strucutre for double-linked node
class DLinkedNode():
    def __init__(self):
        # set the variable for the key (int)
        self.key = 0
        # set the variable for the value (int)
        self.value = 0
        # set the prev pointer
        self.prev = None
        # set the next pointer
        self.next = None


class LRUCache():
    def __init__(self, capacity: int):
        # set the hashmap for cache
        self.cache = {}
        # set the variable for capacity
        self.capacity = capacity
        # create a head and tail pointer
        self.head, self.tail = DLinkedNode(), DLinkedNode()
        # connect the head with the tail
        self.head.next = self.tail
        # connect the tail with the head
        self.tail.prev = self.head

    def get(self, key):
        # if the key does not exist in the cache
        if key not in self.cache:
            # return -1
            return -1
        # update the key as the most recently viewed
        self.move_to_head(self.cache[key])
        # return the value of the key
        return self.cache[key].value

    # function for updating the item as the most recently viewed
    def move_to_head(self, node):
        # remove the current item
        self.remove_node(node)
        # add the new item
        self.add_node(node)

    # function for removing the item
    def remove_node(self, node):
        # get the neightbors of the current item
        prev = node.prev
        next = node.next
        # remove the current item by connecting the neighbors
        prev.next = next
        next.prev = prev

    # function for adding a new item
    def add_node(self, node):
        # connnect the new item with the head pointer
        node.prev = self.head
        # connect the new item with the most recently viewed item
        node.next = self.head.next
        # update the most recently viewed item as the second item
        self.head.next.prev = node
        # connect the head pointer with the new item
        self.head.next = node

    def put(self, key, value):
        # if the key is not part of the cache
        if key not in self.cache:
            # create a new item
            newNode = DLinkedNode()
            newNode.value = value
            newNode.key = key
            # add in the dictionary
            self.cache[key] = newNode
            # add in the double linked node
            self.add_node(newNode)
            # if the size of the cache exceeds the capacity remove the least accessed node
            if len(self.cache.keys()) > self.capacity:
                # get the key of the least recently viewed item
                tail = self.tail.prev
                # remove the key from the node
                self.remove_node(tail)
                # delete the key from the cache
                del self.cache[tail.key]
        # if the key is part of the cache
        else:
            # update the cache
            self.cache[key].value = value
            # update the item as the most recently viewed
            self.move_to_head(self.cache[key])

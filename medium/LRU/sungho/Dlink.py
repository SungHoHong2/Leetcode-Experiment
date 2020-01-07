class DLinkedNode():
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None


class LRUCache():
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.size = 0
        self.head, self.tail = DLinkedNode(), DLinkedNode()

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):

        # get the node from the dictionary
        if key not in self.cache:
            return -1

        # note that DlinkedNode is cached thus it is required to identify the value
        self.move_to_head(self.cache[key])
        return self.cache[key].value

    def move_to_head(self, node):
        self.remove_node(node)
        self.add_node(node)

    def remove_node(self, node):

        # get the neighbors of the node
        prev = node.prev
        new = node.next

        # remove the link of the node
        prev.next = new
        new.prev = prev

    def add_node(self, node):

        # update the node to the first
        node.prev = self.head
        node.next = self.head.next

        # push the original first node to the second
        self.head.next.prev = node
        self.head.next = node

    def put(self, key, value):

        # get the node from the dictonary
        if key not in self.cache:

            newNode = DLinkedNode()
            newNode.value = value
            newNode.key = key

            # add in the dictionary
            self.cache[key] = newNode
            # add in the double linked node
            self.add_node(newNode)
            # increase the size
            self.size += 1

            # if the size of the cache exceeds the capacity remove the least accessed node
            if self.size > self.capacity:
                tail = self.pop_tail()
                del self.cache[tail.key]
                self.size -= 1

        else:
            # if the node exist update the value
            self.cache[key].value = value
            self.move_to_head(self.cache[key])

    def pop_tail(self):
        # get the last node of the list and remove
        res = self.tail.prev
        self.remove_node(res)
        return res
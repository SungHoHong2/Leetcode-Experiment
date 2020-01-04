class DLinkedNode():
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.size = 0
        self.capacity = capacity
        self.head, self.tail = DLinkedNode(), DLinkedNode()

        # head -> tail
        self.head.next = self.tail

        # head <- tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:

        node = self.cache.get(key, None)
        if not node:
            return -1

        self._move_to_head(node)
        return node.value

    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_node(node)

    def _remove_node(self, node):

        # prev <- node -> new
        prev = node.prev
        new = node.next

        # prev -> new
        prev.next = new
        # prev <- new
        new.prev = prev

    def _add_node(self, node):

        # head <- node -> head.next
        node.prev = self.head
        node.next = self.head.next

        # head -> node <- head.next
        self.head.next.prev = node
        self.head.next = node

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key, None)

        node = self.cache.get(key)

        if not node:
            newNode = DLinkedNode()
            newNode.key = key
            newNode.value = value

            self.cache[key] = newNode
            self._add_node(newNode)
            self.size += 1

            if self.size > self.capacity:
                tail = self._pop_tail()
                del self.cache[tail.key]
                self.size -= 1
        else:
            node.value = value
            self._move_to_head(node)

    def _pop_tail(self):

        # tail.prev <- tail
        res = self.tail.prev
        self._remove_node(res)
        return res

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
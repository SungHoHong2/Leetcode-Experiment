class Node(object):
    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.pre = None
        self.next = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.remain = capacity
        self.dic = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.pre = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dic:
            n = self.dic[key]

            self.remove(n)
            self.add(n)
            return n.value
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.dic:
            self.remove(self.dic[key])

        else:
            if self.remain > 0:

                self.remain -= 1
            else:
                self.dic.pop(self.tail.pre.key)
                self.remove(self.tail.pre)

        n = Node(key, value)
        self.add(n)
        self.dic[key] = n

    def add(self, node):
        tmp = self.head.next
        self.head.next = node
        node.pre = self.head
        node.next = tmp
        tmp.pre = node

    def remove(self, node):
        tmp = node.pre
        tmp.next = node.next
        node.next.pre = tmp

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
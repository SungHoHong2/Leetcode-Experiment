class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dic = collections.OrderedDict()
        self.remain = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dic:
            v = self.dic.pop(key)
            self.dic[key] = v
            return v
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.dic:
            self.dic.pop(key)
        else:
            if self.remain <= 0:
                self.dic.popitem(last=False)
            self.remain -= 1

        self.dic[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
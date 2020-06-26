from collections import OrderedDict

class LRUCache():
    def __init__(self, capacity: int):
        # create OrderedDict which is a combination of hashap and linked-list
        self.cache = OrderedDict()
        # pointer to the total size of the LRU
        self.capacity = capacity

    def get(self, key):

        # if there is no key
        if key not in self.cache:
            return -1

        # set the item to most recently checked
        self.cache.move_to_end(key)

        # return the result from the hashmap
        return self.cache[key]

    def put(self, key, value):

        # if the key exists
        if key in self.cache:
            # set the item to most recently checked
            self.cache.move_to_end(key)

        # update the. value
        self.cache[key] = value

        # if the total capacity of the LRU is full remove the least recently checked
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
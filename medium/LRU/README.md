### LRU Cache

**Ordered dictionary**
- [source code](source/OrderedDict.py)

```python
from collections import OrderedDict

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
- [source code](source/)


### Insert Delete GetRandom O(1)
**HashMap + ArrayList**
- [Source code](source/MapList.py)
```python
class RandomizedSet:

    def __init__(self):
        # set up the map
        # set up the list
        pass

    def insert(self, val: int) -> bool:
        # if the inserted item is already in the map
            # return false
        # add key as the inserted item and the total length of the list as the value to the map
        # append to inserted item to the list
        # return true
        pass 

    def remove(self, val: int) -> bool:
        # if the item is in the hashmap
            # get the latest item appended in the list
            # get the index of the removing item
            # override the removing item with the latest item in the list and the map
            # delete the lastest index in the array
            # delete the removing item in the map
            # return true
        # return false
        pass

    def getRandom(self) -> int:
        # use the built-in random.choice function to return the item from the list
        pass
```
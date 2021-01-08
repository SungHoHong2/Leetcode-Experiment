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
        # return false if the inserted item is already in the hashmap
        # add key as the inserted item and value as the future index of the array to the hashmap
        # append inserted item to the array
        # return true
        pass

    def remove(self, val: int) -> bool:
        # if the item is in the hashmap
            # get the latest item appended in the array
            # get the index of the removing item
            # override the removing item with the latest item in the array
            # update latest item in the map with the index of the removing item
            # delete the latest index in the array
            # delete the removing item in the map
            # return true
        # return false if there is no item in the hashmap
        pass

    def getRandom(self) -> int:
        # use the built-in random.choice function to return the item from the list
        pass
```
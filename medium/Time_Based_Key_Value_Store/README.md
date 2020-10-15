### Time Based Key-Value Store
**HashMap + Binary Search**
- [Source code](source/HashBinary.py)
```python
class TimeMap:
    def __init__(self):
        # initialize a map that uses the list as a value
        pass

    def set(self, key: str, value: str, timestamp: int) -> None:
        # append the key and the value
        pass 

    def get(self, key: str, timestamp: int) -> str:
        # return empty string if the key is not in the map
        # bisect.bisect function to return the position of requested timestamp in the sorted list (Note that bisect requires the list to be already sorted)
        # return the result of the value if not return empty string
        pass
```



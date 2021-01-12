### Time Based Key-Value Store
**HashMap + Binary Search**
- Concept 
    - Apply a map that stores the timestamp and the values 
    - Use binary search to search the value according to the timestamp
- Time Complexity
- Space Complexity
- [Source code v3](source/HashBinary3.py)
- [Source code v2](source/HashBinary2.py)
- [Source code v1](source/HashBinary.py)

```python
class TimeMap:
    def __init__(self):
        # initialize a map that uses the list as a value
        pass

    def set(self, key: str, value: str, timestamp: int) -> None:
        # append the key and the value
        pass

    def get(self, key: str, timestamp: int) -> str:
        # return an emtpy string if there is a key in the hashmap
        # get the history of the key 
        # set the pointers for binary search 
        # return empty if the earliest history is later than the requested timestamp 
        # return the latest history if it is earlier than the requested timestamp 
        # start binary search 
            # get the pivot
            # return the pivot if it equals to the timestamp  
            # explore the leftside if the timestamp is larger than the pivot 
            # explore the rightside if the timestamp is smaller than the pivot
        # return the value of the right index
        pass
```



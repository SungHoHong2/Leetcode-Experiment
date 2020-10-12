### Find Duplicate File in System
**Using HashMap**
- [Source code](source/Hashmap.py)
```python
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        # set up the map that uses the content as the key and the list of filenames as the value
        # iterate the paths from the input
            # split the paths into (directory, filenames)
            # place the directory
            # set up a list to store the directory+filename
            # iterate the filenames
                # get the filename
                # get the content
                # append the directory+filename to the list
                # store the content as the key and value as the list
        # return files that contain duplicates
        pass
```

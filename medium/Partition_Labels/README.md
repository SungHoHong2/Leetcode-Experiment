### Partition Labels
**Greedy**
- Concepts
    - For each letter encountered, process the last occurrence of that letter, 
        - extending the current partition [anchor, j] appropriately.
- [Source code](source/Greedy.py)

```python
class Solution(object):
    def partitionLabels(self, S):
        # create a hashmap that collects the rightmost index of the character
        # set the index that records the rightmost index and the next starting point
        # set the returning array 
        # iterate the input 
            # record the maximum rightmost index 
            # if the rightmost index equals to the current index 
                # append the length of the shortest substring
                # mark the starting point of the next substring 
        # return the lengths of the partitioned substrings
        pass
```